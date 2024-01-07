import os
import jiwer

from document.document import Document

class SimilarityResult:
    def __init__(self):
        # representing no errors
        self.wer = 0.0
        self.mer = 0.0
        self.wil = 0.0
        self.wip = 1.0
        self.truth = ""
        self.line = ""

    def calculate(self, truth="", line=""):
        self.truth = truth
        self.line = line

        if (truth.isspace() and line.isspace()) or (truth == "" and line == ""):
            return

        if (truth.isspace() or line.isspace()) or (truth == "" or line == ""):
            # representing errors
            self.wer = 1.0
            self.mer = 1.0
            self.wil = 1.0
            self.wip = 0.0
            return

        output = jiwer.process_words(self.truth, self.line)
        self.wer = output.wer
        self.mer = output.mer
        self.wil = output.wil
        self.wip = output.wip

    def __str__(self):
        return f"WER:{self.wer:.2f} MER:{self.mer:.2f} WIL:{self.wil:.2f} WIP:{self.wip:.2f}\n{self.truth}\n{self.line}\n" 

        

class Similarity:
    def __init__(self):
        self.overall = SimilarityResult()
        self.sentences = []

    def calculate(self, truth_document: Document, document: Document):
        """Calculates the similarity between two documents."""
        truth_doc_lines = Document.sentence_by_sentence(truth_document, add_headers=False, include_time=False)
        doc_lines = Document.sentence_by_sentence(document, add_headers=False, include_time=False)

        whole_truth = ""
        whole = ""
        document_sentence_index = 0
        for index, truth_line in enumerate(truth_doc_lines):
            if index >= len(doc_lines):
                line = ""
            else:
                line = doc_lines[index]

            whole_truth += truth_line + " "
            whole += line + " "

            result = SimilarityResult()
            result.calculate(truth_line, line)
            self.sentences.append(result)
            document_sentence_index += 1

        # copy the rest of the sentences from document2
        for i in range(document_sentence_index, len(doc_lines)):
            truth_line = " "
            line = doc_lines[i]
            whole_truth += truth_line
            whole += line + " "

            result = SimilarityResult()
            result.calculate(truth_line, line)
            self.sentences.append(result)

        self.overall.calculate(whole_truth, whole)

        return self