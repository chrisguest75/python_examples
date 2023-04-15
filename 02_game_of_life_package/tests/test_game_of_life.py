from board import Board


def test_board_constructs_from_state():
    # Arrange
    board = Board([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    # Act
    # Assert
    assert board.width == 3
    assert board.height == 3
    assert len(board.cells) == 3
    # lambda to check each row is the correct length
    assert all(len(row) == 3 for row in board.cells)
    assert board.cells[0] == [1, 0, 0]
    assert board.cells[1] == [0, 1, 0]
    assert board.cells[2] == [0, 0, 1]


def test_summary_empty():
    board = Board([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    assert board.sum_adjacent(1, 1, board.cells) == 0


def test_summary_all():
    board = Board([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
    assert board.sum_adjacent(1, 1, board.cells) == 8


def test_summary_example():
    board = Board([[1, 0, 1], [1, 1, 1], [0, 1, 1]])
    assert board.sum_adjacent(1, 1, board.cells) == 6


def test_summary_vertical():
    board = Board([[0, 1, 0], [0, 1, 0], [0, 1, 0]])
    assert board.sum_adjacent(1, 1, board.cells) == 2


def test_board_step_boat():
    # Arrange
    board = Board(
        [
            [0, 0, 0, 0, 0],
            [0, 1, 1, 0, 0],
            [0, 1, 0, 1, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
        ]
    )
    # Act
    # Assert
    assert board.width == 5
    assert board.height == 5

    board.step()

    assert board.cells[0] == [0, 0, 0, 0, 0]
    assert board.cells[1] == [0, 1, 1, 0, 0]
    assert board.cells[2] == [0, 1, 0, 1, 0]
    assert board.cells[3] == [0, 0, 1, 0, 0]
    assert board.cells[4] == [0, 0, 0, 0, 0]


def test_board_step_blinker():
    # Arrange
    board = Board(
        [
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
        ]
    )
    # Act
    # Assert
    assert board.width == 5
    assert board.height == 5
    assert len(board.cells) == 5
    # lambda to check each row is the correct length
    assert all(len(row) == 5 for row in board.cells)
    assert board.cells[0] == [0, 0, 0, 0, 0]
    assert board.cells[1] == [0, 0, 1, 0, 0]
    assert board.cells[2] == [0, 0, 1, 0, 0]
    assert board.cells[3] == [0, 0, 1, 0, 0]
    assert board.cells[4] == [0, 0, 0, 0, 0]

    board.step()

    assert board.cells[0] == [0, 0, 0, 0, 0]
    assert board.cells[1] == [0, 0, 0, 0, 0]
    assert board.cells[2] == [0, 1, 1, 1, 0]
    assert board.cells[3] == [0, 0, 0, 0, 0]
    assert board.cells[4] == [0, 0, 0, 0, 0]


def test_board_step_overlap():
    # Arrange
    board = Board(
        [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1],
            [0, 0, 0, 0, 1],
            [0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0],
        ]
    )
    # Act
    # Assert
    assert board.width == 5
    assert board.height == 5

    board.step()

    assert board.cells[0] == [0, 0, 0, 0, 0]
    assert board.cells[1] == [0, 0, 0, 0, 0]
    assert board.cells[2] == [1, 0, 0, 1, 1]
    assert board.cells[3] == [0, 0, 0, 0, 0]
    assert board.cells[4] == [0, 0, 0, 0, 0]

    board.step()

    assert board.cells[0] == [0, 0, 0, 0, 0]
    assert board.cells[1] == [0, 0, 0, 0, 1]
    assert board.cells[2] == [0, 0, 0, 0, 1]
    assert board.cells[3] == [0, 0, 0, 0, 1]
    assert board.cells[4] == [0, 0, 0, 0, 0]
