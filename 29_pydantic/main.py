import argparse
import io
import logging
import logging.config
import sys
import traceback
import yaml
import os
from datetime import datetime
from fruit import Fruit
from meeting import Meeting, Address
from pydantic import ValidationError

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
    logger.info(f"Invoked test function - TEST_CONFIG={test_config!r}")

    print(
        Fruit(
            name='Apple',
            color='red',
            weight=4.2,
            bazam={'foobar': [(1, True, 0.1)]},
        )
    )

    # print(
    #     Fruit(
    #         name='Sky',
    #         color='blue',
    #         weight=4.2,
    #         bazam={'foobar': [(1, True, 0.1)]},
    #     )
    # )

    print(Meeting.model_json_schema())

    # m = Meeting.model_validate({'when': '2020-01-01T12:00', 'where': 'home', 'why': 'world'})
    # print(m)

    try:
        m = Meeting.model_validate(
            {'when': datetime.now(), 'where': Address('1','2','3')}, strict=True
        )
    except ValidationError as e:
        print(e)

    logging.info("Finished")
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
