from argparse import ArgumentParser
import os
import random

from typing import List

import cursor
from screen import Screen

def get_cell(items: List[bool], row, col, height, width) -> bool:
    if 0 <= row < height and 0 <= col < width:
        return items[(row*width)+col]
    else:
        return False


def next_generation(cells: List[bool], height: int, width: int):
    cells_copy = cells.copy()
    for i in range(height):
        for j in range(width):
            cell = get_cell(cells_copy, i, j, height, width)
            adjacent = 0

            for n in range(-1,2):
                for m in range(-1,2):
                    if (n == -1 and i == 0) or (m == -1 and j == 0) or (n == 0 and m == 0):
                        continue
                    adjacent += int(get_cell(cells_copy, i+n, j+m, height, width))

            if cell:
                if adjacent < 2:
                    cell = False
                if adjacent > 3:
                    cell = False
            else:
                if adjacent == 3:
                    cell = True

            cells[(i*width)+j] = cell

def run_game(screen: Screen, generations: int = -1):
    cells: List[bool] = [bool(random.getrandbits(1)) for _ in range(screen.size_1d)]

    if generations == -1:
        while True:
            screen.draw(cells)
            cursor.move_up(screen.height)
            next_generation(cells, screen.height, screen.width)
    else:
        for _ in range(generations):
            screen.draw(cells)
            cursor.move_up(screen.height)
            next_generation(cells, screen.height, screen.width)

def main():
    parser = ArgumentParser()
    parser.add_argument("--size", help="Screen size [WxH]")
    parser.add_argument("--generations", help="Number of generations to run")
    args = parser.parse_args()

    if args.size:
        columns, lines = args.size.split("x")
        columns = int(columns)
        lines = int(lines)
    else:
        columns, lines = os.get_terminal_size()
        lines = lines - 1
        columns = int(columns / 2)

    screen = Screen(lines, columns)
    if args.generations:
        run_game(screen, int(args.generations))
    else:
        run_game(screen)

if __name__ == "__main__":
    main()
    