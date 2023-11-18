import argparse
import io
import logging
import logging.config
import sys
import traceback
import yaml
import json
import os
import csv
from pymongo import MongoClient
from datetime import datetime
from jinja2 import Environment, FileSystemLoader
from query_files import query_files
from load_batch_jobs import load_batch_jobs

def log_uncaught_exceptions(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return

    logging.critical("Exception", exc_info=(exc_type, exc_value, exc_traceback))
    logging.critical(
        "Unhandled Exception {0}: {1}".format(exc_type, exc_value),
        extra={"exception": "".join(traceback.format_tb(exc_traceback))},
    )


def str2bool(v):
    return v.lower() in ("yes", "true", "t", "1")


def main():
    with io.open(
        f"{os.path.dirname(os.path.realpath(__file__))}/logging_config.yaml"
    ) as f:
        logging_config = yaml.load(f, Loader=yaml.FullLoader)

    logging.config.dictConfig(logging_config)
    logger = logging.getLogger()

    sys.excepthook = log_uncaught_exceptions

    parser = argparse.ArgumentParser(description="Mongo")
    parser.add_argument("--process", type=str, help="Which process to run query_files|load_batch_jobs")
    parser.add_argument("--config", type=str, help="Configuration file")
    args = parser.parse_args()
    # load configuration file
    config = {}
    # check if query file exists
    if not os.path.isfile(args.config):
        logger.error("Config file does not exist")
        exit(1)    

    with io.open(args.config) as f:
        config = json.load(f)

    if args.process == "query_files":
        if not args.mongo or args.mongo == "":
            parser.print_help()
            exit(1)

        # check if query file exists
        if not os.path.isfile(args.query):
            logger.error("Query file does not exist")
            exit(1)
                
        query_files(args.mongo, args.query, args.db, args.collection)

    if args.process == "load_batch_jobs":
        load_batch_jobs(config)


if __name__ == "__main__":
    main()
    exit(0)
