import argparse
import io
import logging
import logging.config
import sys
import traceback
import yaml
import json
import os
from pymongo import MongoClient


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


def query(connection: str, query: str, db: str, collection: str):
    logger = logging.getLogger()
    client = MongoClient(connection)

    # load query from file
    with open(query, "r") as f:
        query = f.read()
    # convert json string to dict safely
    query = json.loads(query)

    db_obj = client[db]
    collection_obj = db_obj[collection]
    # Execute the query
    cursor = collection_obj.find(query)

    for document in cursor:
        logger.info(document)

def main():
    with io.open(
        f"{os.path.dirname(os.path.realpath(__file__))}/logging_config.yaml"
    ) as f:
        logging_config = yaml.load(f, Loader=yaml.FullLoader)

    logging.config.dictConfig(logging_config)
    logger = logging.getLogger()

    sys.excepthook = log_uncaught_exceptions

    parser = argparse.ArgumentParser(description="Mongo")
    parser.add_argument("--mongo", type=str, help="Connection string")
    parser.add_argument("--query", type=str, help="Query filepath")
    parser.add_argument("--db", type=str, help="Db to query")
    parser.add_argument("--collection", type=str, help="Collection to query")

    args = parser.parse_args()
    if not args.mongo or args.mongo == "":
        parser.print_help()
        exit(1)

    # check if query file exists
    if not os.path.isfile(args.query):
        logger.error("Query file does not exist")
        exit(1)
        
    query(args.mongo, args.query, args.db, args.collection)


if __name__ == "__main__":
    main()
    exit(0)
