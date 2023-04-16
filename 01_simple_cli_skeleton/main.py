import argparse
import io
import logging
import logging.config
import sys
import traceback
import yaml
import os


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


def test():
    logger = logging.getLogger()
    logger.info("Test")


def main():
    with io.open(
        f"{os.path.dirname(os.path.realpath(__file__))}/logging_config.yaml"
    ) as f:
        logging_config = yaml.load(f, Loader=yaml.FullLoader)

    logging.config.dictConfig(logging_config)
    logger = logging.getLogger()

    sys.excepthook = log_uncaught_exceptions

    parser = argparse.ArgumentParser(description="CLI Skeleton")
    parser.add_argument("--test", dest="test", action="store_true")
    args = parser.parse_args()

    if args.test:
        logger.info("Test mode")
        test()
    else:
        parser.print_help()

if __name__ == "__main__":
    print(f"Enter {__name__}")
    main()
    exit(0)
