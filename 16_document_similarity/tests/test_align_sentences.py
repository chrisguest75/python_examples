
from document.document import Document
from process_documents import normalise_document_sentences


def test_alignment_same_document():
    # Arrange
    truth_document = Document()
    truth_document.process_file("./tests/data/test4_a.json")
    test_document = Document()
    test_document.process_file("./tests/data/test4_a.json")
    assert len(truth_document.words) == len(test_document.words)
    # Act
    fixed_truth_document, fixed_test_document = normalise_document_sentences(truth_document, test_document)
    #assert len(truth_document.words) == len(test_document.words)

    # Assert
    assert len(truth_document.sentences) == len(test_document.sentences)

    for i in range(len(truth_document.sentences)):
        assert truth_document.sentences[i] == test_document.sentences[i]

def test_alignment_missing_words():
    pass
#     # Arrange
#     truth_document = Document()
#     truth_document.process_file("./tests/data/test4_a.json")
#     test_document = Document()
#     test_document.process_file("./tests/data/test4_b.json")
#     assert len(truth_document.words) == len(test_document.words)
#     # Act
#     fixed_truth_document, fixed_test_document = normalise_document_sentences(truth_document, test_document)
#     #assert len(truth_document.words) == len(test_document.words)

#     # Assert
#     assert len(truth_document.sentences) == len(test_document.sentences)

#     for i in range(len(truth_document.sentences)):
#         assert truth_document.sentences[i] == test_document.sentences[i]
    
