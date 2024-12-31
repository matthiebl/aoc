"""
--- Day 13: Point of Incidence ---
https://adventofcode.com/2023/day/13
"""

from utils import *

args = parse_args(year=2023, day=13)
raw = get_input(args.filename, year=2023, day=13)

grids = [[list(line) for line in group.splitlines()] for group in raw.split("\n\n")]


def rows_above_reflection(grid: list[list[str]], skip_row: int = 0):
    for i in range(1, len(grid)):
        if i == skip_row:
            continue
        if all(a == b for a, b in zip(grid[i:], grid[:i][::-1])):
            return i
    return 0


p1 = 0
p2 = 0

for grid in grids:
    h = rows_above_reflection(grid)
    v = rows_above_reflection(list(zip(*grid)))
    p1 += h * 100 + v
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            grid[r][c] = "#" if grid[r][c] == "." else "."
            h2 = rows_above_reflection(grid, h)
            v2 = rows_above_reflection(list(zip(*grid)), v)
            grid[r][c] = "#" if grid[r][c] == "." else "."
            if h2 or v2:
                p2 += h2 * 100 + v2
                break
        else:
            continue
        break

print(p1)
print(p2)

if args.test:
    args.tester(p1, p2)
