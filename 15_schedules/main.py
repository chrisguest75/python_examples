import argparse
import io
import logging
import logging.config
import sys
import traceback
import yaml
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
import boto3
from boto3.session import Session
import csv
from datetime import datetime
from jinja2 import Environment, FileSystemLoader

def log_uncaught_exceptions(exc_type, exc_value, exc_traceback):
    """catches unhandled exceptions and logs them"""

    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return

    logging.critical("Exception", exc_info=(exc_type, exc_value, exc_traceback))
    logging.critical(
        "Unhandled Exception {0}: {1}".format(exc_type, exc_value),
        extra={"exception": "".join(traceback.format_tb(exc_traceback))},
    )


def str2bool(value: str) -> bool:
    """ converts strings representing truth to bool """ ""
    return value.lower() in ("yes", "true", "t", "1")


def get_task_details(ecs_client, cluster: str, task_id: str):
    logger = logging.getLogger()
    # Get task details
    task_response = ecs_client.describe_tasks(
        cluster=cluster,
        tasks=[task_id]
    )

    if not task_response['tasks']:
        logger.error(f"Task '{task_id}' not found.")
        return

    task = task_response['tasks'][0]

    arn = task['taskArn']
    task_id = arn.split('/')[2]
    # Format the datetime object as a string without microseconds and timezone information
    formatted_time = task['createdAt'].strftime("%Y-%m-%d %H:%M:%S")


    # Get container details
    container_details = {
        #'task_arn': task['taskArn'],
        'task_id': task_id,
        'desiredStatus': task['desiredStatus'],
        'createdAt': formatted_time,
        #'containers': task['containers'],
    }
    full_task_details = task

    return container_details, full_task_details


def get_tasks(cluster: str, family: str) -> int:
    """test function"""
    logger = logging.getLogger()

    # Replace the following with your own values
    profile_name = os.environ['AWS_PROFILE']

    # Create a session with the specified profile
    session = Session(profile_name=profile_name)
    ecs_client = session.client('ecs')

    response = ecs_client.list_tasks(cluster=cluster, family=family)

    logger.info(response)

    data = []
    for task_arn in response['taskArns']:
        container, task = get_task_details(
            ecs_client, cluster, task_arn)
        logger.info(container)
        logger.info(task)
        data.append(container)

    csv_file_path = "./data/data.csv"

    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        
        header = data[0].keys()
        writer.writerow(header)
        
        for row in data:
            writer.writerow(row.values())

    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('./templates/GANTT.md.j2')
    current_datetime = datetime.now()
    filetime = current_datetime.strftime('%Y%m%d_%H%M%S')
    gantt_path = f"./out/GANTT_{filetime}.md"
    context = {
        'current_datetime': current_datetime,
        'data': data,
        'title': f"{cluster} {family}"
    }
    output = template.render(**context)
    with open(gantt_path, mode='w', newline='') as file:
        file.write(output)


    return 0


def main() -> int:
    """
    main function

    returns 0 on success, 1 on failure

    configures logging and processes command line arguments
    """
    with io.open(
        f"{os.path.dirname(os.path.realpath(__file__))}/logging_config.yaml"
    ) as f:
        logging_config = yaml.load(f, Loader=yaml.FullLoader)

    logging.config.dictConfig(logging_config)

    sys.excepthook = log_uncaught_exceptions

    parser = argparse.ArgumentParser(description="CLI Skeleton")
    parser.add_argument("--render", dest="render", action="store_true")
    parser.add_argument("--cluster", dest="cluster")
    parser.add_argument("--family", dest="family")
    args = parser.parse_args()

    success = 0
    if args.render:
        success = get_tasks(args.cluster, args.family)
    else:
        parser.print_help()

    return success


if __name__ == "__main__":
    # print(f"Enter {__name__}")
    exit(main())
