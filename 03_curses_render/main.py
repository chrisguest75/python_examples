import argparse
import curses
import os
import random
import sys
import game_of_life_package
from game_of_life_package.board import Board
from game_of_life_package.cell_parser import CellParser


def list_cells():
    print("Available cells:")
    files = os.listdir("cells")
    files.sort()
    for file in files:
        if file.endswith(".cells"):
            print(f"  {file}")


def init_color_pairs():
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_BLACK)  # Low
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_WHITE)  # Medium


def draw_grid(stdscr, data):
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


def main(stdscr, cell_path):
    curses.curs_set(0)
    init_color_pairs()

    height, width = stdscr.getmaxyx()
    width //= 2

    # load cell file
    with open(cell_path) as f:
        cell_parser = CellParser()
        # join lines together
        lines = "".join(f.readlines())
        cells = cell_parser.parse(lines)

    # Arrange
    board = Board(width, height)
    board.set_state(0, 0, cells)

    # Set up the terminal
    curses.curs_set(0)
    stdscr.nodelay(True)  # Set getch() to be non-blocking
    stdscr.timeout(100)  # Set getch() to time out after 100ms if there's no input

    while True:
        data = board.cells
        draw_grid(stdscr, data)
        board.step()
        key = stdscr.getch()
        if key == ord("q") or key == ord("Q"):
            break


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Game of Life")
    parser.add_argument(
        "--file",
        type=str,
        help="Path to cell file to load, example: barge2spaceship.cells",
    )
    parser.add_argument(
        "--list", dest="list", action="store_true", help="List cell files"
    )
    parser.add_argument(
        "--info", dest="info", action="store_true", help="Info on cell file"
    )
    parser.add_argument(
        "--version", dest="version", action="store_true", help="Print versions"
    )    
    args = parser.parse_args()

    if args.list:
        list_cells()

    if args.version:
        versions = []
        for module_name, module in sys.modules.items():
            try:
                versions.append((module_name, module.__version__))
            except AttributeError:
                versions.append((module_name, "no version"))
                # This module doesn't have a __version__ attribute
                pass
        print(f"Python version: {sys.version}")
        print(f"Package versions:{versions}")

    elif args.file:
        cell_path = f"{os.path.dirname(os.path.realpath(__file__))}/cells/{args.file}"
        if args.info:
            with open(cell_path) as f:
                print(f.read())
        else:
            curses.wrapper(main, cell_path)
    else:
        parser.print_help()
