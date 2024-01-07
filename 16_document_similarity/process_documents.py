from document.document import Document
import jiwer

def process_documents(paths: list):
    """Processes the documents."""
    documents = []
    for path in paths:
        doc = Document("original")
        doc.process_file(path)
        documents.append(doc)

    return documents


def calculate_similarity(truth_document: Document, document: Document):
    """Calculates the similarity between two documents."""
    truth_doc_lines = Document.sentence_by_sentence(truth_document, add_headers=False, include_time=False)
    doc_lines = Document.sentence_by_sentence(document, add_headers=False, include_time=False)

    results = []
    for index, truth_line in enumerate(truth_doc_lines):
        if index >= len(doc_lines):
            break

        output = jiwer.process_words(truth_line, doc_lines[index])
        wer = output.wer
        mer = output.mer
        wil = output.wil

        result = {}
        result["truth"] = truth_line
        result["line"] = doc_lines[index]
        result["wer"] = wer
        result["mer"] = mer
        result["wil"] = wil
        results.append(result)

    return results
