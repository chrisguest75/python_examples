import argparse
import io
import logging
import logging.config
import sys
import traceback
import yaml
import os

from process_documents import process_documents

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
    logger.info(f"Invoked test function - TEST_CONFIG='{test_config}'")

    file1 = f"./documents/english_windinthewillows_grahame_rll_8khz_16kb_9.2.0.m4a.json"
    file2 = f"./documents/english_windinthewillows_grahame_rll_64kb.mp3.json"

    # Create the "out" folder if it doesn't exist
    if not os.path.exists("./out"):
        os.mkdir("./out")    

    in_paths= [
        file1,
        file2,
    ]

    filename1 = os.path.splitext(os.path.basename(file1))[0]
    filename2 = os.path.splitext(os.path.basename(file2))[0]
    out_paths= [
        filename1,
        filename2,
    ]

    documents = process_documents(in_paths)

    doc_index = 0
    for document in documents:
        output = []
        output.append(f"File: {document.path}")
        for sentence in document.sentences:
            line = ""
            if len(sentence) == 0:
                continue
            start_time = sentence[0]["start_time"]
            end_time = sentence[-1]["end_time"]
            line = f"{start_time:0>9.3f} - {end_time:0>9.3f} "
            start = ""
            for word in sentence:
                if word["type"] == "punctuation":
                    line += word["word"]
                else:
                    line += f"{start}{word['word']}"
                start = " "
            output.append(line)
        
        with open(f"./out/{out_paths[doc_index]}.txt", "w") as file:
            for line in output:
                print(line)
                file.write(line + "\n")
     
        doc_index += 1

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
