import argparse
import io
import logging
import logging.config
import sys
import traceback
import yaml
import json
import os
import platform
import importlib.metadata
from importlib.metadata import distributions
from rembg import remove
from PIL import Image
import cv2
import numpy as np

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


def mask_to_svg_path(mask_image):
    # Ensure the mask is binary
    _, binary_mask = cv2.threshold(mask_image, 127, 255, cv2.THRESH_BINARY)

    # Find contours
    contours, _ = cv2.findContours(binary_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Initialize an SVG path string
    svg_paths = []
    
    for contour in contours:
        path = "M "  # Start an SVG path
        for i, point in enumerate(contour):
            x, y = point[0]
            if i == 0:
                path += f"{x},{y} "
            else:
                path += f"L {x},{y} "
        path += "Z"  # Close the path
        svg_paths.append(path)

    return "\n".join(svg_paths)

def convert_mask_to_svg(inputFile: str, outputFile:str):
    logger = logging.getLogger()

    logger.info(f"Processing {inputFile} to {outputFile}")

    # Load a binary mask (grayscale image)
    mask_image = cv2.imread(inputFile, cv2.IMREAD_GRAYSCALE)

    # Convert to SVG path
    svg_path = mask_to_svg_path(mask_image)
    print(svg_path)

    # Save to a file if needed
    with open(outputFile, "w") as f:
        f.write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {mask_image.shape[1]} {mask_image.shape[0]}">\n')
        f.write(f'<path d="{svg_path}" fill="black" stroke="cyan" stroke-width="10" />\n')
        f.write('</svg>')

    return svg_path

def test(inputFile: str, outputFile:str, convert: str, overwrite:bool) -> int:
    """test function"""
    logger = logging.getLogger()
    test_config = os.environ["TEST_CONFIG"]
    logger.info(f'Invoked test function - TEST_CONFIG={test_config!r}')
    logger.info(f"details={details()}")

    # platform_details = details()
    # for key in platform_details.keys():
    #     logger.info(f"{key}: {platform_details[key]}")

    frame_number = 1
    frames = { 'frames': [] }

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
                
                logger.info(f"Processing {filename} ({count} files remaining)")

                if convert == "background":
                    if filename.endswith(".png") or filename.endswith(".jpg"):
                        pngfilename = filename.replace(".jpg", ".png")

                        if os.path.exists(f"{outputDir}/{pngfilename}") and not overwrite:
                            logger.info(f"Skipping {filename}")
                            count -= 1
                            continue    

                        input = Image.open(f"{inputDir}/{filename}")
                        output = remove(input)
                        # replace extension with .png
                        filename = filename.replace(".jpg", ".png")
                        output.save(f"{outputDir}/{filename}")
                
                elif convert == "mask":
                    if os.path.exists(f"{outputDir}/{filename}") and not overwrite:
                        logger.info(f"Skipping {filename}")
                        count -= 1
                        continue    

                    infile = os.path.join(inputDir, filename)
                    image = Image.open(infile)
                    # Extract the alpha channel
                    alpha_channel = image.getchannel("A")  # "A" stands for Alpha
                    outfile = f"{outputDir}/{filename}"
                    alpha_channel.save(outfile)

                elif convert == "svg":
                    #if os.path.exists(f"{outputDir}/{filename}") and not overwrite:
                    #    logger.info(f"Skipping {filename}")
                    #    count -= 1
                    #    continue    
                                        
                    infile = os.path.join(inputDir, filename)
                    filename = filename.replace(".png", ".svg")
                    outfile = f"{outputDir}/{filename}"
                    svg_path = convert_mask_to_svg(infile, outfile)
                    frame = {
                        "name": filename,
                        "path": svg_path,
                        "number": frame_number
                    }
                    frames['frames'].append(frame)
                    frame_number += 1

                count -= 1

                
    # else:
    #     # remove background
    #     input = Image.open(inputFile)
    #     output = remove(input)

    #     # create directory if not exists
    #     os.makedirs(os.path.dirname(outputFile), exist_ok=True)
    #     output.save(outputFile)

    if convert == "svg":
        with open("./frames.json", "w") as f:
            f.write(json.dumps(frames, indent=4))

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
    parser.add_argument("--convert", dest="convert", type=str, help="svg|background", required=True)
    parser.add_argument("--input", dest="input", type=str, required=True)
    parser.add_argument("--output", dest="output", type=str, required=True)
    parser.add_argument("--overwrite", dest="overwrite", type=bool , default=False)
    args = parser.parse_args()

    success = test(args.input, args.output, args.convert, args.overwrite)

    return success


if __name__ == "__main__":
    # print(f"Enter {__name__}")
    exit(main())




