import unittest
from codeartifact_test_package.metadata import get_metadata

class TestMetadata(unittest.TestCase):

    def test_metadata_contains_values(self):
        # Arrange
        # Act
        metadata = get_metadata()

        # Assert
        self.assertEqual(metadata.get('name'), 'codeartifact-test-package')

if __name__ == '__main__':
    unittest.main()




