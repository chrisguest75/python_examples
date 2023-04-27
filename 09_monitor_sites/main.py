import argparse
import io
import logging
import logging.config
import sys
import traceback
import yaml
import json
import os
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


def start_monitor(monitor_config: str) -> list[Interval]:
    """monitor function"""
    logger = logging.getLogger()
    print(f"monitor_config: {monitor_config}")
    # configure each of the monitors
    intervals = []
    try:
        logger.info(f"monitor_config: {monitor_config}")

        # each site is a separate object
        for name in monitor_config["sites"]:
            logger.info(f"name: {name}")
            site_config = monitor_config["sites"][name]
            # put namne into site_config object
            site_config["name"] = name
            endpoint = Endpoint(**site_config)
            if endpoint.enabled:
                logger.info(f"{name} is enabled")
                logger.info(f"site: {endpoint}")

                if endpoint.verb.upper() == "GET":
                    # start the interval
                    interval = Interval(endpoint)
                    intervals.append(interval)
                    interval.start()
                else:
                    logger.warning(f"{endpoint.verb} is not supported")
            else:
                logger.info(f"{name} is disabled")

    except Exception as e:
        logger.critical(f"Exception: {e}")
        raise

    return intervals


def main() -> int:
    """
    main function

    returns 0 on success, 1 on failure

    configures logging and processes command line arguments
    """
    success = 0
    parser = argparse.ArgumentParser(description="Monitor sites")
    parser.add_argument(
        "--monitor", dest="monitor", action="store_true", help="start monitoring"
    )
    parser.add_argument(
        "--sites",
        dest="sites",
        help="sites configuration json file",
        type=str,
        default=f"{os.path.dirname(os.path.realpath(__file__))}/monitor.json",
    )
    args = parser.parse_args()

    try:
        with io.open(
            f"{os.path.dirname(os.path.realpath(__file__))}/logging_config.yaml"
        ) as f:
            logging_config = yaml.load(f, Loader=yaml.FullLoader)

        logging.config.dictConfig(logging_config)

        sys.excepthook = log_uncaught_exceptions

    except FileNotFoundError as e:
        print(f"Missing logging_config.yaml")
        print(e)
        success = 1
        return success

    logger = logging.getLogger()

    try:
        if args.monitor:
            # get the monitor config file path
            try:
                monitor_config_file = os.environ["MONITOR_CONFIG"]
            except KeyError:
                monitor_config_file = args.sites

            # load the monitor config file
            with io.open(monitor_config_file) as f:
                monitor_config = json.load(f)

            intervals = start_monitor(monitor_config)

            # Wait to exit here?  Or sleep infinity?
            input("Press Enter to quit.....")

            logger.info("Shutting down.....")

            for interval in intervals:
                interval.stop()

            logger.info("Waiting to stop.....")
        else:
            parser.print_help()
    except Exception as e:
        print(f"Failed during monitoring with {e}")
        success = 1

    return success


if __name__ == "__main__":
    exit(main())
