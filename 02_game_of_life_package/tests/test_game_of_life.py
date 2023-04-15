from board import Board


def test_board_constructs_empty():
    # Arrange
    board = Board(5, 5)
    # Act
    # Assert
    assert board.width == 5
    assert board.height == 5
    assert board.cells.length == 5
    # lambda to check each row is the correct length
    assert all(len(row) == 5 for row in board.cells)
