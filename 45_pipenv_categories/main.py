import argparse
import io
import logging
import logging.config
import sys
import traceback
import yaml
import os
import platform
import pprint
import torch
import importlib.metadata

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

def details() -> str:
    """ return details about python version and platform as a dict """
    return {
        "python_version": sys.version,
        "platform": sys.platform,
        "platform_details": platform.platform(),
    }


def str2bool(value: str) -> bool:
    """ converts strings representing truth to bool """ ""
    return value.lower() in ("yes", "true", "t", "1")


def is_cuda():
    out = []
    out.append(f'cuda.is_available: {torch.cuda.is_available()}')
    out.append(f'importlib.metadata.version("torch"): {importlib.metadata.version("torch")}')
    pprint.pp(out)
    return out 

def is_working():
    out = []
    t = torch.rand(5, 3)
    out.append(str(t))
    out.append(f'shape: {t.shape}')
    out.append(f'dtype: {t.dtype}')
    out.append(f'device: {t.device}')
    pprint.pp(out)
    return out 

def test() -> int:
    """test function"""
    logger = logging.getLogger()
    test_config = os.environ["TEST_CONFIG"]
    logger.info(f'Invoked test function - TEST_CONFIG={test_config!r}')
    logger.info(f"details={details()}")
    is_cuda()
    is_working()
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