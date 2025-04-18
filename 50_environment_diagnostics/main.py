import argparse
import io
import logging
import logging.config
import sys
import traceback
import yaml
import os
import platform
from importlib.metadata import distributions
from cpuinfo import get_cpu_info
from pynvml import nvmlInit, nvmlSystemGetDriverVersion, nvmlDeviceGetCount, nvmlDeviceGetHandleByIndex, nvmlDeviceGetName


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

def linux_distribution():
  try:
    return platform.linux_distribution()
  except:
    return "N/A"

def dist():
  try:
    return platform.dist()
  except:
    return "N/A"

def details() -> str:
    """return details about python version and platform as a dict"""

    platform_details = {
        "platform": {
            "python_version": sys.version,
            "platform": sys.platform,
            "platform_details": platform.platform(),
            "dist": str(dist()),
            "linux_distribution": linux_distribution(),
            "system": platform.system(),
            "machine": platform.machine(),
            "uname": platform.uname(),
            "version": platform.version(),
            "mac_ver": platform.mac_ver(),
        }
    }
    platform_details["cpu"] = {}
    for key, value in get_cpu_info().items():
        platform_details["cpu"][key] = value

    platform_details["packages"] = {}
    installed_packages = [(dist.metadata["Name"], dist.version) for dist in distributions()]
    for package in installed_packages:
        platform_details["packages"][package[0]] = package[1]

    platform_details["gpu"] = {}
    platform_details["gpu"]["device_count"] = 0
    try:      
        nvmlInit()
        platform_details["gpu"]["driver_version"] = nvmlSystemGetDriverVersion()
        deviceCount = nvmlDeviceGetCount()
        platform_details["gpu"]["device_count"] = deviceCount

        for i in range(deviceCount):
            handle = nvmlDeviceGetHandleByIndex(i)
            platform_details["gpu"][f"device_{i}"] = nvmlDeviceGetName(handle)
    except Exception as e:
        logging.error(f"Error getting GPU details: {e}")

    return platform_details


def str2bool(value: str) -> bool:
    """ converts strings representing truth to bool """ ""
    return value.lower() in ("yes", "true", "t", "1")


def test() -> int:
    """test function"""
    logger = logging.getLogger()
    test_config = os.environ["TEST_CONFIG"]
    logger.info(f"Invoked test function - TEST_CONFIG={test_config!r}")
    logger.info(f"details={details()}")

    platform_details = details()
    for group in platform_details.keys():
        for key in platform_details[group].keys():
            logger.info({ "message": "environment diagnostic", f"{group}.{key}": platform_details[group][key] })

    return 0


def main() -> int:
    """
    main function

    returns 0 on success, 1 on failure

    configures logging and processes command line arguments
    """
    with io.open(f"{os.path.dirname(os.path.realpath(__file__))}/logging_config.yaml") as f:
        logging_config = yaml.load(f, Loader=yaml.FullLoader)

    logging.config.dictConfig(logging_config)

    sys.excepthook = log_uncaught_exceptions

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
