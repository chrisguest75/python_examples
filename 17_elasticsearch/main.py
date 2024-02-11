import argparse
import io
import logging
import logging.config
import sys
import traceback
import yaml
import os

from elasticsearch import Elasticsearch
from typing import List

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

def find_md_files(directory: str) -> List[str]:
    """Find all .md files in a directory and its subdirectories"""
    md_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                md_files.append(os.path.join(root, file))
    return md_files

def load_md_files(es, files):
    """Load all .md files into Elasticsearch"""

    for file in files:
        logging.info(f"Loading {file}")
        with open(file, 'r') as f:
            content = f.read()
            doc = {
                "content": content,
                "title": file,
                "date": "2023-02-01"
            }
            res = es.index(index="markdown_documents", document=doc)
            logging.info(res['result'])
    

def load() -> int:
    """test function"""
    logger = logging.getLogger()
    test_config = os.environ["TEST_CONFIG"]
    logger.info(f"Invoked test function - TEST_CONFIG='{test_config}'")


    files = find_md_files("../")
    logging.info(f"Found {len(files)} markdown files")

    try:
        # Initialize Elasticsearch client
        es = Elasticsearch("http://0.0.0.0:9200")

        load_md_files(es, files)
    except Exception as e:
        logging.error(f"Error: {e}")
        return 1

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

    parser = argparse.ArgumentParser(description="Elasticsearch")
    parser.add_argument("--load", dest="load", action="store_true")
    args = parser.parse_args()

    success = 0
    if args.load:
        success = load()
    else:
        parser.print_help()

    return success


if __name__ == "__main__":
    # print(f"Enter {__name__}")
    exit(main())





