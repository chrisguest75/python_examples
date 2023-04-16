import curses
import random
from game_of_life_package.board import Board

def init_color_pairs():
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)   # Low
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_WHITE)  # Medium

def generate_data(height, width):
    return [[random.randint(0, 100) for _ in range(width)] for _ in range(height)]

def draw_heatmap(stdscr, data):
    max_y, max_x = stdscr.getmaxyx()
    max_x //= 2

    for y, row in enumerate(data):
        if y >= max_y - 1:
            break

        for x, value in enumerate(row):
            if x >= max_x - 1:
                break

            if value == 0:
                color_pair = 1
            elif value == 1:
                color_pair = 2

            stdscr.addstr(y, x * 2, "  ", curses.color_pair(color_pair))
    stdscr.refresh()



def main(stdscr):
    curses.curs_set(0)
    init_color_pairs()

    height, width = stdscr.getmaxyx()
    width //= 2

    # Arrange
    board = Board(width, height)
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

    # Set up the terminal
    curses.curs_set(0)
    stdscr.nodelay(True)  # Set getch() to be non-blocking
    stdscr.timeout(100)  # Set getch() to time out after 100ms if there's no input

    while True:
        data = board.cells
        draw_heatmap(stdscr, data)
        board.step()
        key = stdscr.getch()
        if key == ord("q") or key == ord("Q"):
            break

if __name__ == "__main__":
    curses.wrapper(main)
