from document.document import Document

def process_documents(paths: list):
    """Processes the documents."""
    documents = []
    for path in paths:
        doc = Document("original")
        doc.process_file(path)
        documents.append(doc)

    return documents