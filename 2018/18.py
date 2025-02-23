"""
--- Day 18: Settlers of The North Pole ---
https://adventofcode.com/2018/day/18
"""

from utils import *

args = parse_args(year=2018, day=18)
raw = get_input(args.filename, year=2018, day=18)

grid = [list(line) for line in raw.splitlines()]
R, C = len(grid), len(grid[0])

p1 = 0
p2 = 0

values = []
for t in range(1000):
    new_grid = create_grid(R, C)
    trees, lumberyards = 0, 0
    for (r, c), v, _ in enumerate_grid(grid):
        adjacent = [adj for _, adj in neighbours(grid, r, c, request=8)]
        if v == ".":
            new_grid[r][c] = "|" if adjacent.count("|") >= 3 else "."
        elif v == "|":
            new_grid[r][c] = "#" if adjacent.count("#") >= 3 else "|"
            trees += 1
        else:
            new_grid[r][c] = "#" if (adjacent.count("#") >= 1 and adjacent.count("|") >= 1) else "."
            lumberyards += 1
    grid = new_grid

    value = trees * lumberyards
    if t == 10:
        p1 = value
    if t > 500 and value == values[0]:
        break
    if t >= 500:
        values.append(value)

print(p1)

p2 = values[(1000000000 - 500) % len(values)]
print(p2)

if args.test:
    args.tester(p1, p2)
