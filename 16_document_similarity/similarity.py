import os
import jiwer

from document.document import Document

class SimilarityResult:
    def __init__(self):
        self.wer = 0
        self.mer = 0
        self.wil = 0
        self.wip = 0
        self.truth = ""
        self.line = ""

    def calculate(self, truth="", line=""):
        self.truth = truth
        self.line = line
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

        self.overall.calculate(whole_truth, whole)

        return self