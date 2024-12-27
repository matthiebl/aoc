"""
--- Day 3: Gear Ratios ---
https://adventofcode.com/2023/day/3
"""

from utils import *

args = parse_args(year=2023, day=3)
raw = get_input(args.filename, year=2023, day=3)

grid = [list(line) for line in raw.splitlines()]

p2 = 0
seen = {}
part_value = {}
part_num = 0

for (r, c), val, _ in enumerate_grid(grid, skip=".0123456789"):
    for dr, dc in directions(8):
        nr, nc = r + dr, c + dc
        if not within_grid(grid, nr, nc) or not grid[nr][nc] in "0123456789" or (nr, nc) in seen:
            continue
        while within_grid(grid, nr, nc - 1) and grid[nr][nc - 1] in "0123456789":
            nc -= 1
        n = 0
        while within_grid(grid, nr, nc) and grid[nr][nc] in "0123456789":
            n = n * 10 + int(grid[nr][nc])
            seen[(nr, nc)] = part_num
            nc += 1
        part_value[part_num] = n
        part_num += 1

    if val != "*":
        continue
    parts = set(seen[(r + dr, c + dc)] for dr, dc in directions(8) if (r + dr, c + dc) in seen)
    if len(parts) == 2:
        p2 += mul(part_value[n] for n in parts)

p1 = sum(n for n in part_value.values())
print(p1)
print(p2)

if args.test:
    args.tester(p1, p2)
