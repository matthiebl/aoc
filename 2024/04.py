"""
--- Day 4: Ceres Search ---
https://adventofcode.com/2024/day/4
"""

from utils import *

args = parse_args(year=2024, day=4)
raw = get_input(args["filename"], year=2024, day=4)

grid = [list(line) for line in raw.splitlines()]
R, C = len(grid), len(grid[0])

p1 = 0
for r in range(R):
    for c in range(C):
        if grid[r][c] != "X":
            continue
        for dr, dc in directions(8):
            search = "X"
            for i in range(1, 4):
                if not (0 <= r + dr * i < R and 0 <= c + dc * i < C):
                    break
                search += grid[r + dr * i][c + dc * i]
            else:
                if search == "XMAS":
                    p1 += 1
print(p1)

p2 = 0
for r in range(1, R - 1):
    for c in range(1, C - 1):
        down, up = list(chunks(directions("X"), 3))
        if ("".join([grid[r + dr][c + dc] for dr, dc in down]) in ["MAS", "SAM"]
                and "".join([grid[r + dr][c + dc] for dr, dc in up]) in ["MAS", "SAM"]):
            p2 += 1
print(p2)

assert p1 == 2530
assert p2 == 1921
