class Board:
    def __init__(self, board: list[list[int]]):
        self.width = len(board[0])
        self.height = len(board)
        self.cells = board

    def sum_adjacent(self, x: int, y: int, cells: list[list[int]]) -> int:
        count = 0
        row1 = y - 1 if y - 1 >= 0 else self.height - 1
        row2 = y
        row3 = y + 1 if y + 1 < self.height else 0
        col1 = x - 1 if x - 1 >= 0 else self.width - 1
        col2 = x
        col3 = x + 1 if x + 1 < self.width else 0

        if cells[row1][col1] >= 1:
            count += 1
        if cells[row1][col2] >= 1:
            count += 1
        if cells[row1][col3] >= 1:
            count += 1
        if cells[row2][col1] >= 1:
            count += 1
        # if cells[y][x] >= 1: count += 1
        if cells[row2][col3] >= 1:
            count += 1
        if cells[row3][col1] >= 1:
            count += 1
        if cells[row3][col2] >= 1:
            count += 1
        if cells[row3][col3] >= 1:
            count += 1

        return count

    def step(self):
        cells = [[0 for _ in range(self.width)] for _ in range(self.height)]

        for y in range(self.height):
            # if y >= 1 and y < (self.height - 1):
            for x in range(self.width):
                # if x >= 1 and x < (self.width - 1):
                count = self.sum_adjacent(x, y, self.cells)
                if self.cells[y][x] == 1:
                    if count < 2:
                        cells[y][x] = 0
                    if count == 2 or count == 3:
                        cells[y][x] = 1
                    if count > 3:
                        cells[y][x] = 0
                else:
                    if count == 3:
                        cells[y][x] = 1
        self.cells = cells
