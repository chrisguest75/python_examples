from a02_game_of_life_package.board import Board


def test_board_constructs_empty():
    # Arrange
    board = Board(3, 3)
    assert board.width == 3
    assert board.height == 3
    assert len(board.cells) == 3
    # Act
    # Assert
    # lambda to check each row is the correct length
    assert all(len(row) == 3 for row in board.cells)
    # assert all cells are 0
    assert all(all(cell == 0 for cell in row) for row in board.cells)


def test_board_sets_state():
    # Arrange
    board = Board(3, 3)
    assert board.width == 3
    assert board.height == 3
    assert len(board.cells) == 3
    # Act
    board.set_state(0, 0, [[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    # Assert
    # lambda to check each row is the correct length
    assert all(len(row) == 3 for row in board.cells)
    assert board.cells[0] == [1, 0, 0]
    assert board.cells[1] == [0, 1, 0]
    assert board.cells[2] == [0, 0, 1]


def test_summary_empty():
    # Arrange
    board = Board(3, 3)
    # Act
    board.set_state(0, 0, [[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    # Assert
    assert board.sum_adjacent(1, 1, board.cells) == 0


def test_summary_all():
    # Arrange
    board = Board(3, 3)
    # Act
    board.set_state(0, 0, [[1, 1, 1], [1, 1, 1], [1, 1, 1]])
    # Assert
    assert board.sum_adjacent(1, 1, board.cells) == 8


def test_summary_example():
    # Arrange
    board = Board(3, 3)
    # Act
    board.set_state(0, 0, [[1, 0, 1], [1, 1, 1], [0, 1, 1]])
    # Assert
    assert board.sum_adjacent(1, 1, board.cells) == 6


def test_summary_vertical():
    # Arrange
    board = Board(3, 3)
    # Act
    board.set_state(0, 0, [[0, 1, 0], [0, 1, 0], [0, 1, 0]])
    # Assert
    assert board.sum_adjacent(1, 1, board.cells) == 2


def test_board_step_boat():
    # Arrange
    board = Board(5, 5)
    board.set_state(
        0,
        0,
        [
            [0, 0, 0, 0, 0],
            [0, 1, 1, 0, 0],
            [0, 1, 0, 1, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
        ],
    )
    # Act
    board.step()
    # Assert
    assert board.cells[0] == [0, 0, 0, 0, 0]
    assert board.cells[1] == [0, 1, 1, 0, 0]
    assert board.cells[2] == [0, 1, 0, 1, 0]
    assert board.cells[3] == [0, 0, 1, 0, 0]
    assert board.cells[4] == [0, 0, 0, 0, 0]


def test_board_step_blinker():
    # Arrange
    board = Board(5, 5)
    board.set_state(
        0,
        0,
        [
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
        ],
    )
    # Act
    board.step()

    assert board.cells[0] == [0, 0, 0, 0, 0]
    assert board.cells[1] == [0, 0, 0, 0, 0]
    assert board.cells[2] == [0, 1, 1, 1, 0]
    assert board.cells[3] == [0, 0, 0, 0, 0]
    assert board.cells[4] == [0, 0, 0, 0, 0]


def test_board_step_overlap():
    # Arrange
    board = Board(5, 5)
    board.set_state(
        0,
        0,
        [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1],
            [0, 0, 0, 0, 1],
            [0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0],
        ],
    )
    # Act
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
