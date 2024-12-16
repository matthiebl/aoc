"""
--- Day 6: Guard Gallivant ---
https://adventofcode.com/2024/day/6
"""

from utils import *

args = parse_args(year=2024, day=6)
raw = get_input(args.filename, year=2024, day=6)

grid = [list(line) for line in raw.splitlines()]
R, C = len(grid), len(grid[0])

D = directions("cw4")

guard = None
for r, row in enumerate(grid):
    if "^" in row:
        guard = (r, row.index("^"))
        break


def traverse(start: tuple[int, int], p2: bool = False):
    path = set([start])
    turns = set()
    r, c = start
    d = 0  # index in D
    while True:
        dr, dc = D[d]
        if not within_grid(grid, r + dr, c + dc):
            return path, False
        if grid[r + dr][c + dc] == "#":
            if (r, c, d) in turns:
                return path, True
            turns.add((r, c, d))
            d = (d + 1) % 4
        else:
            r, c = r + dr, c + dc
        if not p2:
            path.add((r, c))


path, _ = traverse(guard)
p1 = len(path)
print(p1)

p2 = 0
for r, c in path:
    if grid[r][c] != ".":
        continue
    grid[r][c] = "#"
    if traverse(guard, p2=True)[1]:
        p2 += 1
    grid[r][c] = "."
print(p2)

if args.test:
    args.tester(p1, p2)
