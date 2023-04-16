from game_of_life_package.cell_parser import CellParser


def test_parser_empty_file():
    # Arrange
    parser = CellParser()

    # Act
    cells = parser.parse("")

    # Assert
    assert cells == []


def test_parser_only_headers_file():
    # Arrange
    parser = CellParser()

    # Act
    example = """
!Name: test
!Author: Chris Guest
!Simple block
!no comment
"""
    cells = parser.parse(example)

    # Assert
    assert cells == []


def test_loader_simple_file():
    # Arrange
    parser = CellParser()

    # Act
    example = """!Name: test
!Author: Chris Guest
!Simple block
!no comment
OOO
OOO
OOO
"""

    cells = parser.parse(example)

    # Assert
    assert len(cells) == 3
    assert all(len(row) == 3 for row in cells)
    assert cells[0] == [1, 1, 1]
    assert cells[1] == [1, 1, 1]
    assert cells[2] == [1, 1, 1]


def test_loader_mixed_length_rows_file():
    # Arrange
    parser = CellParser()

    # Act
    example = """!Name: test
!Author: Chris Guest
!Simple block
!no comment
OOO.O...
OOO.......
OO..O....
"""

    cells = parser.parse(example)

    # Assert
    assert len(cells) == 3
    assert all(len(row) == 10 for row in cells)
    assert cells[0] == [1, 1, 1, 0, 1, 0, 0, 0, 0, 0]
    assert cells[1] == [1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
    assert cells[2] == [1, 1, 0, 0, 1, 0, 0, 0, 0, 0]
