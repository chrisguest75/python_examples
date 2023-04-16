class CellParser:
    def __init__(self) -> None:
        pass

    def parse(self, file: str) -> list[list[int]]:
        cells = []
        # use a lambda to filter lines that are empty or start with !
        lines = [
            line for line in file.splitlines() if line and not line.startswith("!")
        ]
        if len(lines) > 0:
            max_line = max(len(line) for line in lines)

            for line in lines:
                row = [1 if c == "O" else 0 for c in line]
                row += [0] * (max_line - len(line))
                cells.append(row)

            # print(cells)

        return cells
