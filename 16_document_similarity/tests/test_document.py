
from document.document import Document

def test_load_words():
    # Arrange
    doc = Document("./documents/test1.json")

    assert len(doc.words) == 2
    assert doc.words[0]["word"] == "Extract"
    assert doc.words[1]["word"] == "from"    

def test_confidence_selection():
    # Arrange
    doc = Document("./documents/test2.json")

    assert len(doc.words) == 2
    assert doc.words[0]["word"] == "Extract"
    assert doc.words[1]["word"] == "from"


