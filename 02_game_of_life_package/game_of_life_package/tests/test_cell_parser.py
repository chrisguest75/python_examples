from a02_game_of_life_package.cell_parser import CellParser

def test_parser_empty_file():
    # Arrange
    parser = CellParser()

    # Act
    cells = parser.parse('')

    # Assert
    assert cells == []

def test_parser_only_headers_file():
    # Arrange
    parser = CellParser()

    # Act
    example = '''
!Name: test
!Author: Chris Guest
!Simple block
!no comment
'''    
    cells = parser.parse(example)

    # Assert
    assert cells == []


def test_loader_simple_file():
    # Arrange
    parser = CellParser()

    # Act
    example = '''
!Name: test
!Author: Chris Guest
!Simple block
!no comment
OOO
OOO
OOO
    '''

    cells = parser.parse(example)

    # Assert
    assert cells == []
