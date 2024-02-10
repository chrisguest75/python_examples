import argparse
import io
import logging
import logging.config
import sys
import traceback
import yaml
import os

from elasticsearch import Elasticsearch

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


def test() -> int:
    """test function"""
    logger = logging.getLogger()
    test_config = os.environ["TEST_CONFIG"]
    logger.info(f"Invoked test function - TEST_CONFIG='{test_config}'")

    # Initialize Elasticsearch client
    es = Elasticsearch("http://localhost:9200")

    # Define the index name
    index_name = "markdown_documents"

    # Read Markdown file
    markdown_file_path = 'README.md'
    with open(markdown_file_path, 'r') as file:
        markdown_content = file.read()

    # Document to be indexed
    doc = {
        "content": markdown_content,  # or markdown_content if you prefer raw Markdown
        "title": "README",  # Extract or define your title
        "date": "2023-02-01"  # Define or extract the date
    }

    # Index the document
    res = es.index(index=index_name, document=doc)

    # Output the result
    logging.info(res['result'])

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
    parser.add_argument("--test", dest="test", action="store_true")
    args = parser.parse_args()

    success = 0
    if args.test:
        success = test()
    else:
        parser.print_help()

    return success


if __name__ == "__main__":
    # print(f"Enter {__name__}")
    exit(main())





