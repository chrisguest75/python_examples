import argparse
import io
import logging
import logging.config
import sys
import traceback
import yaml
import os


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


def main(event, context) -> int:
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

    logging.info(dir(event))
    queryStringParameters = event.get('queryStringParameters', None)
    if queryStringParameters is None:
        logging.error("URL is required")
        return 'Please provide a url as a query string parameter'
    
    url = queryStringParameters.get('url', None)
    if url is None:
        logging.error("URL is required")
        return 'Please provide a url as a query string parameter'
    
    return {"url": url, 'version': sys.version, 'event': event}


def handler(event, context):
    return main(event, context)

