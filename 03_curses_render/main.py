import curses
import random

def init_color_pairs():
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)   # Low
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_GREEN)  # Medium
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_RED)    # High

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

            if value < 33:
                color_pair = 1
            elif value < 66:
                color_pair = 2
            else:
                color_pair = 3

            stdscr.addstr(y, x * 2, "  ", curses.color_pair(color_pair))
    stdscr.refresh()



def main(stdscr):
    curses.curs_set(0)
    init_color_pairs()

    height, width = stdscr.getmaxyx()
    width //= 2

    while True:
        data = generate_data(height, width)
        draw_heatmap(stdscr, data)

        key = stdscr.getch()
        if key == ord("q") or key == ord("Q"):
            break

if __name__ == "__main__":
    curses.wrapper(main)
