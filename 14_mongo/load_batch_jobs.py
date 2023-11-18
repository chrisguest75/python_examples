import logging
import boto3
from boto3.session import Session
from pymongo import MongoClient
from datetime import datetime

def list_all_jobs(batch_client, queue_name: str, job_status: str):
    """List all jobs for a specific queue and status, handling pagination."""
    next_token = None
    all_jobs = []

    while True:
        # If next_token is None, it fetches the first page
        if next_token:
            response = batch_client.list_jobs(jobQueue=queue_name, jobStatus=job_status, nextToken=next_token)
        else:
            response = batch_client.list_jobs(jobQueue=queue_name, jobStatus=job_status)

        all_jobs.extend(response.get('jobSummaryList', []))

        # Check if there is a next token; if not, break the loop
        next_token = response.get('nextToken')
        if not next_token:
            break

    processed_jobs = []
    today = datetime.now().date()
    for job in all_jobs:
        userid = job['jobName'][:24]
        created = job['createdAt'] / 1000
        started = job.get('startedAt', 0) / 1000
        stopped = job.get('stoppedAt', 0) / 1000
        createdAt = datetime.fromtimestamp(created)
        startedAt = datetime.fromtimestamp(started)
        stoppedAt = datetime.fromtimestamp(stopped)

        processed_jobs.append({
            'createdAt': createdAt.strftime("%Y-%m-%d %H:%M:%S"),
            'startedAt': startedAt.strftime("%Y-%m-%d %H:%M:%S"),
            'stoppedAt': stoppedAt.strftime("%Y-%m-%d %H:%M:%S"),
            'jobName': job['jobName'],
            'processingTime': (stopped - started) if stopped and started else None,
            'queueTime': (started - created) if started else None,
            'totalTime': (stopped - created) if stopped else None,
            'jobId': job['jobId'],
            'userId': userid
        })

    return processed_jobs

def get_jobs_schedules(batch_client, queue_name: str) -> int:
    """test function"""
    logger = logging.getLogger()

    response = batch_client.describe_job_queues()
    for queue in response.get('jobQueues', []):
        logger.info(f"Queue Name: {queue['jobQueueName']}, Status: {queue['state']}")

    logger.info(f"Using '{queue_name}'")
    # Example usage: List all SUBMITTED jobs in the specified queue
    processed_jobs = list_all_jobs(batch_client, queue_name, 'SUCCEEDED')

    logger.info(f"Found {len(processed_jobs)} jobs")
    
    return processed_jobs


def load_batch_jobs(config: dict):
    logger = logging.getLogger() 
    connection = config['MONGO_CONNECTION']
    db = config['MONGO_DB']
    collection = config['MONGO_COLLECTION']

    client = MongoClient(connection)
    db_obj = client[db]
    collection_obj = db_obj[collection]

    # Replace the following with your own values
    profile_name = config['AWS_PROFILE']
    region = config['AWS_REGION']

    queue_name = config['QUEUE_NAME']

    # Create a session with the specified profile
    session = Session(profile_name=profile_name, region_name=region)
    batch_client = session.client('batch')

    processed_jobs = get_jobs_schedules(batch_client, queue_name)

    logging.info(processed_jobs[0])

    # insert into mongo
    collection_obj.insert_many(processed_jobs)

    # get latest and record the latest date

    # update recrods 

    # do partial updates
