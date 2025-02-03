"""
--- Day 19: A Series of Tubes ---
https://adventofcode.com/2017/day/19
"""

from utils import *

args = parse_args(year=2017, day=19)
raw = get_input(args.filename, year=2017, day=19)

grid = [list(line) for line in raw.splitlines()]
r, c = next(find_in_grid(grid, "|"))
r -= 1
dr, dc = 1, 0

p1 = ""
p2 = -1
while True:
    nr, nc = r + dr, c + dc
    p2 += 1
    if grid[nr][nc] == " ":
        break
    if grid[nr][nc] != "+":
        if grid[nr][nc] not in "|-":
            p1 += grid[nr][nc]
    elif dr != 0:
        if grid[nr][nc - 1] != " ":
            dr, dc = 0, -1
        else:
            dr, dc = 0, 1
    elif grid[nr - 1][nc] != " ":
        dr, dc = -1, 0
    else:
        dr, dc = 1, 0
    r, c = nr, nc
print(p1)
print(p2)

if args.test:
    args.tester(p1, p2)
