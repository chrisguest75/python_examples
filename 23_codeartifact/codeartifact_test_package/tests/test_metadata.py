from codeartifact_test_package.metadata import get_metadata

def test_metadata_contains_values():
    # Arrange
    # Act
    metadata = get_metadata()

    # Assert
    assert metadata.get('name') == 'codeartifact-test-package'
    assert metadata.get('description') == 'A test package for CodeArtifact'




