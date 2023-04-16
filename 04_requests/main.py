import argparse
import io
import logging
import logging.config
import sys
import traceback
import yaml
import os
from simple import simple_get


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


def simple(url: str):
    logger = logging.getLogger()
    logger.info("Test")
    response = simple_get(url)
    logger.info(response)

def main():
    with io.open(
        f"{os.path.dirname(os.path.realpath(__file__))}/logging_config.yaml"
    ) as f:
        logging_config = yaml.load(f, Loader=yaml.FullLoader)

    logging.config.dictConfig(logging_config)
    logger = logging.getLogger()

    sys.excepthook = log_uncaught_exceptions

    parser = argparse.ArgumentParser(description="Requests")
    parser.add_argument("--simple", dest="simple", action="store_true")
    parser.add_argument(
        "--url",
        type=str,
        help="Endpoint to invoke",
    )
    args = parser.parse_args()
    if not args.url or args.url == "":
        parser.print_help()
        exit(1)

    if args.simple:
        logger.info("Simple")
        simple(args.url)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
    exit(0)
