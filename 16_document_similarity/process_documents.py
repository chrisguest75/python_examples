import os
import jiwer

from document.document import Document

def normalise_document_sentences(truth_document: Document, test_document: Document) -> (Document, Document):
    truth_filename = os.path.basename(truth_document.path)
    test_filename = os.path.basename(test_document.path)

    fixed_test_document1 = align_sentences(truth_document, test_document, f"{test_filename}_aligned_1")
    fixed_test_document2 = align_sentences(test_document, fixed_test_document1, f"{test_filename}_aligned_2")

    fixed_truth_document1 = align_sentences(test_document, truth_document, f"{truth_filename}_aligned_1")
    fixed_truth_document2 = align_sentences(truth_document, fixed_truth_document1, f"{truth_filename}_aligned_2")

    return fixed_truth_document2, fixed_test_document2


def align_sentences(document1: Document, document2: Document, name: str, threshold=0.25) -> Document:
    '''
    Aligns the sentences in document1 with the sentences in document2.
    Takes a sentence and a sentence from document2 and compares the start and end times.
    If the start and end times are within the threshold, the sentences are considered a match.
    If the start and end times are not within the threshold, the sentences are not considered a match and the next sentence endtime is compared.
    '''
    output = []
    # create a new document to hold the aligned sentences
    fixed_document = Document(name, document2.base)
    fixed_document.path = name
    document2_sentence_index = 0

    for sentence in document1.sentences:
        if len(sentence) == 0:
            continue

        start_time = sentence[0]["start_time"]
        end_time = sentence[-1]["end_time"]
        if document2_sentence_index >= len(document2.sentences) or len(document2.sentences[document2_sentence_index]) == 0:
            line1 = Document.sentence_to_line(sentence)
            line2 = ""
            output.append(line1)
            output.append(line2)
            document2_sentence_index += 1
            continue
        
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

    # copy the rest of the sentences from document2
    for i in range(document2_sentence_index, len(document2.sentences)):
        fixed_document.sentences.append(document2.sentences[i])

    return fixed_document


