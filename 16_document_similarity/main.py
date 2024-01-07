import argparse
import io
import logging
import logging.config
import sys
import traceback
import yaml
import os

from document.document import Document
from process_documents import calculate_similarity, normalise_document_sentences

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


def process_documents(truth_document_path: str, test_document_path: str) -> int:
    """test function"""
    logger = logging.getLogger()
    #test_config = os.environ["TEST_CONFIG"]
    #logger.info(f"Invoked test function - TEST_CONFIG='{test_config}'")

    # Create the "out" folder if it doesn't exist
    if not os.path.exists("./out"):
        os.mkdir("./out")    

    truth_document = Document("truth", truth_document_path)
    truth_document.process_file(truth_document_path)
    test_document = Document("test", test_document_path)
    test_document.process_file(test_document_path)

    fixed_truth_document, fixed_test_document = normalise_document_sentences(truth_document, test_document)

    documents = []
    documents.append(fixed_truth_document)

    # the b documents are now aligned with each other.  
    documents.append(fixed_test_document)

    for document in documents:
        out_path = os.path.splitext(os.path.basename(document.path))[0]

        output = Document.sentence_by_sentence(document)
        with open(f"./out/{out_path}.txt", "w") as file:
            for line in output:
                print(line)
                file.write(line + "\n")    

    write_similarity_results(fixed_truth_document, fixed_test_document, f"./out/results_1_2.txt")

    return 0


def write_similarity_results(truth_document: Document, document: Document, out_path: str):
    results = calculate_similarity(truth_document, document)
    with open(out_path, "w") as file:
        for result in results:
            file.write(f"WER:{result['wer']:.2f} MER:{result['mer']:.2f} WIL:{result['wil']:.2f} WIP:{result['wip']:.2f}\n")  
            file.write(f"{result['truth']}\n")
            file.write(f"{result['line']}\n")
            print(f"WER:{result['wer']:.2f} MER:{result['mer']:.2f} WIL:{result['wil']:.2f} WIP:{result['wip']:.2f}")
            print(f"{result['truth']}")
            print(f"{result['line']}")


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

    parser = argparse.ArgumentParser(description="Process documents")
    parser.add_argument("--truth", dest="truth", type=str, help="The source of truth document we're aiming to match")
    parser.add_argument("--test", dest="test", type=str, help="The document to test against the truth document")
    parser.add_argument("--process", dest="process", action="store_true", help="Process the documents" )
    args = parser.parse_args()

    success = 0
    if args.process:
        success = process_documents(args.truth, args.test)
    else:
        parser.print_help()

    return success


if __name__ == "__main__":
    # print(f"Enter {__name__}")
    exit(main())
