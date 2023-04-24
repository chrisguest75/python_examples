import argparse
import io
import logging
import logging.config
import sys
import traceback
import yaml
import json
import os
import time
from interval import Interval
from endpoint import Endpoint


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


def monitor() -> int:
    """monitor function"""
    logger = logging.getLogger()

    try:
        monitor_config_file = os.environ["MONITOR_CONFIG"]
    except KeyError:
        monitor_config_file = (
            f"{os.path.dirname(os.path.realpath(__file__))}/monitor.json"
        )

    try:
        with io.open(monitor_config_file) as f:
            monitor_config = json.load(f)

        logger.info(f"monitor_config: {monitor_config}")

        intervals = []

        for name in monitor_config["sites"]:
            logger.info(f"name: {name}")
            site_config = monitor_config["sites"][name]
            site_config["name"] = name
            endpoint = Endpoint(**site_config)

            logger.info(f"site: {endpoint}")

            interval = Interval(endpoint)
            intervals.append(interval)
            interval.start()

        input("Press Enter to continue...")

        for interval in intervals:
            interval.stop()

        logger.info("Quitting.....")

    except Exception as e:
        logger.critical(f"Exception: {e}")

    return 0


def main() -> int:
    """
    main function

    returns 0 on success, 1 on failure

    configures logging and processes command line arguments
    """
    success = 0
    parser = argparse.ArgumentParser(description="Monitor sites")

    try:
        with io.open(
            f"{os.path.dirname(os.path.realpath(__file__))}/logging_config.yaml"
        ) as f:
            logging_config = yaml.load(f, Loader=yaml.FullLoader)

        logging.config.dictConfig(logging_config)

        sys.excepthook = log_uncaught_exceptions

        parser.add_argument(
            "--monitor", dest="monitor", action="store_true", help="start monitoring"
        )
        args = parser.parse_args()

        if args.monitor:
            success = monitor()
        else:
            parser.print_help()
    except Exception as e:
        print("Missing logging_config.yaml")
        success = 1

    return success


if __name__ == "__main__":
    exit(main())
