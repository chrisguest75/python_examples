import argparse
import io
import logging
import logging.config
import sys
import traceback
import yaml
import os
import tarfile


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

format_to_string = {
    tarfile.USTAR_FORMAT: "USTAR_FORMAT",
    tarfile.GNU_FORMAT: "GNU_FORMAT",
    tarfile.PAX_FORMAT: "PAX_FORMAT",
    tarfile.DEFAULT_FORMAT: "DEFAULT_FORMAT"
}

def check_tar_file(filename):
    if tarfile.is_tarfile(filename):
        print(f"{filename} is a valid tar file.")
        with tarfile.open(filename) as tf:
            format = format_to_string.get(tf.format, "Unknown Format")
            print(f"Type: {format}")
    else:
        print(f"{filename} is not a tar file.")


def info(filePath: str) -> int:
    """test function"""
    logger = logging.getLogger()
    test_config = os.environ["TEST_CONFIG"]
    logger.info(f"Invoked test function - TEST_CONFIG='{test_config}'")

    # Replace 'sample.tar' with your tar file's name
    check_tar_file(filePath)

    list_of_files = []
    with tarfile.open(filePath) as tf:
        for member in tf.getmembers():
            details = {
                "name": member.name,
                "size": member.size,
                "offset": member.offset,
            }
            list_of_files.append(details)

    print(f"Files in {filePath}:")
    for file in list_of_files:
        print(file)
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
    parser.add_argument("--info", dest="info", action="store_true")
    parser.add_argument("--file", dest="file", type=str)
    args = parser.parse_args()

    success = 0
    if args.info:
        success = info(args.file)
    else:
        parser.print_help()

    return success


if __name__ == "__main__":
    # print(f"Enter {__name__}")
    exit(main())
