import argparse
import io
import logging
import logging.config
import sys
import traceback
import yaml
import os

from process_documents import process_documents, calculate_similarity
from document.document import Document

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


def align_sentences(document1, document2, name: str, threshold=0.25):
    output = []
    fixed_document = Document(name, document2.base)
    fixed_document.path = name
    document2_sentence_index = 0

    for sentence in document1.sentences:
        if len(sentence) == 0:
            continue

        start_time = sentence[0]["start_time"]
        end_time = sentence[-1]["end_time"]

        d2_start_time = document2.sentences[document2_sentence_index][0]["start_time"]
        d2_end_time = document2.sentences[document2_sentence_index][-1]["end_time"]
    
        if abs(start_time - d2_start_time) <= threshold and abs(end_time - d2_end_time) <= threshold:
            # Start time is within the threshold
            output.append(f"Match: {start_time:0>9.3f} - {end_time:0>9.3f} with {d2_start_time:0>9.3f} - {d2_end_time:0>9.3f}")

            line1 = Document.sentence_to_line(sentence)
            line2 = Document.sentence_to_line(document2.sentences[document2_sentence_index])
            fixed_document.sentences.append(document2.sentences[document2_sentence_index])
            output.append(line1)
            output.append(line2)

            document2_sentence_index += 1
        else:
            # Start time is not within the threshold
            #output.append(f"No match: {start_time:0>9.3f} - {end_time:0>9.3f} with {d2_start_time:0>9.3f} - {d2_end_time:0>9.3f}")
            start_index = document2_sentence_index
            line2 = []

            for i in range(start_index, len(document2.sentences)):
                if len(document2.sentences[i]) == 0:
                    continue
                d2_end_time = document2.sentences[i][-1]["end_time"]
                line2 = line2 + document2.sentences[i]

                if abs(end_time - d2_end_time) <= threshold:
                    output.append(f"Match: {start_time:0>9.3f} - {end_time:0>9.3f} with {d2_start_time:0>9.3f} - {d2_end_time:0>9.3f}")
                    output.append(Document.sentence_to_line(sentence))
                    output.append(Document.sentence_to_line(line2))
                    fixed_document.sentences.append(line2)
                    document2_sentence_index = i + 1
                    break

    # with open(f"./out/compare_{name}.txt", "w") as file:
    #     for line in output:
    #         print(line)
    #         file.write(line + "\n")

    return fixed_document


def test() -> int:
    """test function"""
    logger = logging.getLogger()
    test_config = os.environ["TEST_CONFIG"]
    logger.info(f"Invoked test function - TEST_CONFIG='{test_config}'")

    file1 = f"./documents/english_windinthewillows_grahame_rll_64kb.mp3.json"
    file2 = f"./documents/english_windinthewillows_grahame_rll_8khz_16kb_9.2.0.m4a.json"

    # Create the "out" folder if it doesn't exist
    if not os.path.exists("./out"):
        os.mkdir("./out")    

    in_paths= [
        file1,
        file2,
    ]

    documents = process_documents(in_paths)
    document1 = documents[0]
    document2 = documents[1]

    fixed_document1_a = align_sentences(document1, document2, "english_windinthewillows_grahame_rll_64kb_1")
    fixed_document2_a = align_sentences(document2, fixed_document1_a, "english_windinthewillows_grahame_rll_64kb_2")

    fixed_document1_b = align_sentences(document2, document1, "english_windinthewillows_grahame_rll_8khz_16kb_9.2.0_1")
    fixed_document2_b = align_sentences(document1, fixed_document1_b, "english_windinthewillows_grahame_rll_8khz_16kb_9.2.0_2")


    documents.append(fixed_document1_a)
    documents.append(fixed_document2_a)

    # the b documents are now aligned with each other.  
    documents.append(fixed_document1_b)
    documents.append(fixed_document2_b)

    for document in documents:
        out_path = os.path.splitext(os.path.basename(document.path))[0]

        output = Document.sentence_by_sentence(document)
        with open(f"./out/{out_path}.txt", "w") as file:
            for line in output:
                print(line)
                file.write(line + "\n")    

    write_similarity_results(fixed_document2_a, fixed_document2_b, f"./out/results_1_2.txt")
    write_similarity_results(fixed_document2_b, fixed_document2_a, f"./out/results_2_1.txt")


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
