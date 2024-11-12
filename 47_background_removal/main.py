import argparse
import io
import logging
import logging.config
import sys
import traceback
import yaml
import os
import platform
import importlib.metadata
from importlib.metadata import distributions
from rembg import remove
from PIL import Image

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
    """return details about python version and platform as a dict"""

    platform_details = {
        "python_version": sys.version,
        "platform": sys.platform,
        "platform_details": platform.platform(),
    }

    installed_packages = [(dist.metadata["Name"], dist.version) for dist in distributions()]
    for package in installed_packages:
        platform_details[package[0]] = package[1]

    return platform_details


def str2bool(value: str) -> bool:
    """ converts strings representing truth to bool """ ""
    return value.lower() in ("yes", "true", "t", "1")


def test(inputFile: str, outputFile:str) -> int:
    """test function"""
    logger = logging.getLogger()
    test_config = os.environ["TEST_CONFIG"]
    logger.info(f'Invoked test function - TEST_CONFIG={test_config!r}')
    logger.info(f"details={details()}")

    platform_details = details()
    for key in platform_details.keys():
        logger.info(f"{key}: {platform_details[key]}")
    
    # is inputFile a directory?
    if os.path.isdir(inputFile):
        # iterate over a directory of images
        inputDir = inputFile
        outputDir = outputFile
        os.makedirs(outputDir, exist_ok=True)

        # get count of files in directory
        files = os.listdir(inputDir) 
        count = len(files)
        # sort files
        files.sort()
        
        # iterate over a directory of images
        for filename in files:
            if os.path.isfile(os.path.join(inputDir, filename)):
                if filename.endswith(".png") or filename.endswith(".jpg"):
                    logger.info(f"Processing {filename} ({count} files remaining)")
                    input = Image.open(f"{inputDir}/{filename}")
                    output = remove(input)
                    # replace extension with .png
                    filename = filename.replace(".jpg", ".png")
                    output.save(f"{outputDir}/{filename}")
                    count -= 1
    else:
        # remove background
        input = Image.open(inputFile)
        output = remove(input)

        # create directory if not exists
        os.makedirs(os.path.dirname(outputFile), exist_ok=True)
        output.save(outputFile)

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
    parser.add_argument("--input", dest="input", type=str, required=True)
    parser.add_argument("--output", dest="output", type=str, required=True)
    args = parser.parse_args()

    success = test(args.input, args.output)

    return success


if __name__ == "__main__":
    # print(f"Enter {__name__}")
    exit(main())
