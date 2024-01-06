
from document.document import Document

def test_load_words():
    # Arrange
    doc = Document("./documents/test1.json")

    assert len(doc.words) == 0

