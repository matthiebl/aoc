"""
--- Day 11: Cosmic Expansion ---
https://adventofcode.com/2023/day/11
"""

from utils import *

args = parse_args(year=2023, day=11)
raw = get_input(args.filename, year=2023, day=11)

grid = [list(line) for line in raw.splitlines()]
R, C = len(grid), len(grid[0])


def expand(lines: list[list[str]], increase: int = 2) -> list[int]:
    expansion = []
    i = 0
    for line in lines:
        expansion.append(i)
        if line.count("#") == 0:
            i += increase - 1
    return expansion


galaxies = list(find_in_grid(grid, "#"))

expansion_rows = expand(grid)
expansion_cols = expand(zip(*grid))
p1 = 0
for i, (r1, c1) in enumerate(galaxies):
    for r2, c2 in galaxies[i+1:]:
        p1 += manhattan(r1 + expansion_rows[r1], c1 + expansion_cols[c1],
                        r2 + expansion_rows[r2], c2 + expansion_cols[c2])
print(p1)

expansion_rows = expand(grid, 1000000)
expansion_cols = expand(zip(*grid), 1000000)
p2 = 0
for i, (r1, c1) in enumerate(galaxies):
    for r2, c2 in galaxies[i+1:]:
        p2 += manhattan(r1 + expansion_rows[r1], c1 + expansion_cols[c1],
                        r2 + expansion_rows[r2], c2 + expansion_cols[c2])
print(p2)

if args.test:
    args.tester(p1, p2)
