
from document.document import Document
from process_documents import normalise_document_sentences

def test_alignment_empty_test_document():
    '''
    Test that the alignment works when the test document is empty
    Truth document is full document and test document remains empty
    '''
    # Arrange
    truth_document = Document()
    truth_document.process_file("./tests/data/test4_a.json")
    test_document = Document()
    test_document.process_file("./tests/data/empty.json")
    assert len(test_document.words) == 0
    assert len(test_document.sentences) <= 1
    # Act
    fixed_truth_document, fixed_test_document = normalise_document_sentences(truth_document, test_document)
    #assert len(truth_document.words) == len(test_document.words)

    # Assert
    assert len(fixed_truth_document.sentences) == len(truth_document.sentences)
    assert len(fixed_test_document.sentences) <= len(test_document.sentences)


def test_alignment_same_document():
    '''
    Test that the alignment works when the test document is the same as the truth document
    '''
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
    assert len(fixed_truth_document.sentences) == len(fixed_test_document.sentences)

    for i in range(len(fixed_truth_document.sentences)):
        # both sentences should be exactly the same
        assert fixed_truth_document.sentences[i] == fixed_test_document.sentences[i]

def test_alignment_skipped_words():
    # Arrange
    truth_document = Document()
    truth_document.process_file("./tests/data/test4_a.json")
    test_document = Document()
    test_document.process_file("./tests/data/test4_a_skipped_words.json")
    assert len(truth_document.words) > len(test_document.words)
    # Act
    fixed_truth_document, fixed_test_document = normalise_document_sentences(truth_document, test_document)

    # Assert
    assert len(fixed_truth_document.sentences) == len(fixed_test_document.sentences)
    assert fixed_truth_document.sentences[0] == fixed_test_document.sentences[0]
    assert fixed_truth_document.sentences[-1] == fixed_test_document.sentences[-1]
    

def test_alignment_skipped_grammar():
    # Arrange
    truth_document = Document()
    truth_document.process_file("./tests/data/test4_a.json")
    test_document = Document()
    test_document.process_file("./tests/data/test4_a_skipped_grammar.json")
    assert len(truth_document.words) > len(test_document.words)
    # Act
    fixed_truth_document, fixed_test_document = normalise_document_sentences(truth_document, test_document)

    # Assert
    assert len(fixed_truth_document.sentences) == len(fixed_test_document.sentences)
    # there are grammar differences in the first sentence
    assert fixed_truth_document.sentences[0] != fixed_test_document.sentences[0]
    assert fixed_truth_document.sentences[-1] == fixed_test_document.sentences[-1]

def test_alignment_truth_truncated():
    # Arrange
    truth_document = Document()
    truth_document.process_file("./tests/data/test4_a_truncated.json")
    test_document = Document()
    test_document.process_file("./tests/data/test4_a.json")
    assert len(truth_document.words) < len(test_document.words)
    # Act
    fixed_truth_document, fixed_test_document = normalise_document_sentences(truth_document, test_document)

    # Assert
    assert len(fixed_truth_document.sentences) < len(fixed_test_document.sentences)

def test_alignment_test_truncated():
    # Arrange
    truth_document = Document()
    truth_document.process_file("./tests/data/test4_a.json")
    test_document = Document()
    test_document.process_file("./tests/data/test4_a_truncated.json")
    assert len(truth_document.words) > len(test_document.words)
    # Act
    fixed_truth_document, fixed_test_document = normalise_document_sentences(truth_document, test_document)

    # Assert
    assert len(fixed_truth_document.sentences) > len(fixed_test_document.sentences)