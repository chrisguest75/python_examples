
from document.document import Document

def test_load_words():
    # Arrange
    doc = Document()
    doc.process_file("./tests/data/no_punctuation.json")
    # Assert
    assert len(doc.words) == 2
    assert doc.words[0]["word"] == "Extract" and doc.words[0]["type"] == "word"
    assert doc.words[1]["word"] == "from" and doc.words[1]["type"] == "word"

def test_confidence_selection():
    # Arrange
    doc = Document()
    doc.process_file("./tests/data/alternatives.json")
    # Assert
    assert len(doc.words) == 2
    assert doc.words[0]["word"] == "Extract"
    assert doc.words[1]["word"] == "from"

def test_extract_sentence():
    # Arrange
    doc = Document()
    doc.process_file("./tests/data/two_sentences.json")
    # Assert
    assert len(doc.words) == 5
    assert doc.words[0]["word"] == "Extract" and  doc.words[0]["type"] == "word"
    assert doc.words[1]["word"] == "from" and doc.words[1]["type"] == "word"
    assert doc.words[2]["word"] == "." and doc.words[2]["type"] == "punctuation"
    assert doc.words[3]["word"] == "Hello" and doc.words[3]["type"] == "word"
    assert doc.words[4]["word"] == "world" and doc.words[4]["type"] == "word"

    assert len(doc.sentences) == 2
    assert len(doc.sentences[0]) == 3
    assert len(doc.sentences[1]) == 2

