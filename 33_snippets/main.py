import argparse
import io
import logging
import logging.config
import logging.handlers
import sys
import traceback
from typing import List
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


def test() -> int:
    """test function"""
    logger = logging.getLogger()
    test_config = os.environ["TEST_CONFIG"]
    logger.info(f'Invoked test function - TEST_CONFIG={test_config!r}')
    return 0

class ContextFilter(logging.Filter):
    """
    This is a filter which injects contextual information into the log.
    """
    def __init__(self, attributes: List[str]):
        super().__init__()
        self.attributes = attributes

    def filter(self, record):
        for a in self.attributes:
            setattr(record, a,  os.environ.get(a, 'NOTSET'))
    
        print(f"record: {record}")
        return True
    

    
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

    logger = logging.getLogger()
    logger.addFilter(ContextFilter(['TEST_CONFIG', 'CORRELATION_ID', 'BUILD_ID', 'DOES_NOT_EXIST']))

    logging.info(logging.handlers)
    attached_handlers = logger.handlers

    # Loop through the attached handlers and print them
    for h in attached_handlers:
        logger.info(f"Handler: {h}")

    # You can also access the first handler directly if you know there's only one
    #first_handler = logger.handlers[0]
    #print(f"First attached handler: {first_handler}")

    #



    parser = argparse.ArgumentParser(description="CLI Skeleton")
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
