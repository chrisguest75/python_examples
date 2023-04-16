import argparse
import io
import logging
import logging.config
import sys
import traceback
import yaml
import os
from simple import simple_get
from timeout import timeout_get
from post import post_data


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
    logger.info("Simple Test")
    response = simple_get(url)
    logger.info(response)


def timeout(url: str, timeout_seconds: int = 5):
    logger = logging.getLogger()
    logger.info("Timeout Test")
    response = timeout_get(url, timeout_seconds)
    logger.info(response)


def post(url: str, data: str):
    logger = logging.getLogger()
    logger.info("Post Test")
    response = post_data(url, data)
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
    parser.add_argument(
        "--url",
        type=str,
        help="Endpoint to invoke",
    )
    parser.add_argument("--simple", dest="simple", action="store_true")
    parser.add_argument(
        "--timeout",
        type=int,
        help="Timeout in seconds",
    )
    parser.add_argument(
        "--post",
        type=str,
        help="Post data",
    )
    args = parser.parse_args()
    if not args.url or args.url == "":
        parser.print_help()
        exit(1)

    if args.simple:
        simple(args.url)
    elif args.timeout:
        timeout(args.url, args.timeout)
    elif args.post:
        post(args.url, args.post)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
    exit(0)
