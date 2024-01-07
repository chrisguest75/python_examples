
from document.document import Document
from process_documents import normalise_document_sentences
from similarity import Similarity, SimilarityResult

def test_similarity_same_document():
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
    
    results = Similarity().calculate(fixed_truth_document, fixed_test_document)
    assert len(results.sentences) == 177
    assert results.overall.wer == 0
    assert results.overall.mer == 0
    assert results.overall.wil == 0
    assert results.overall.wip == 1.0

def test_similarity_empty_document():
    '''
    Test that the alignment works when the test document is the same as the truth document
    '''
    # Arrange
    truth_document = Document()
    truth_document.process_file("./tests/data/test4_a.json")
    test_document = Document()
    test_document.process_file("./tests/data/empty.json")
    assert len(test_document.words) == 0
    # Act
    fixed_truth_document, fixed_test_document = normalise_document_sentences(truth_document, test_document)
    #assert len(truth_document.words) == len(test_document.words)

    # Assert
    assert len(fixed_truth_document.sentences) == len(truth_document.sentences)
    
    results = Similarity().calculate(fixed_truth_document, fixed_test_document)
    assert len(results.sentences) == 177
    assert results.overall.wer == 1.0
    assert results.overall.mer == 1.0
    assert results.overall.wil == 1.0
    assert results.overall.wip == 0.0


