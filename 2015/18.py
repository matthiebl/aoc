"""
--- Day 18: Like a GIF For Your Yard ---
https://adventofcode.com/2015/day/18
"""

from utils import *

args = parse_args(year=2015, day=18)
raw = get_input(args.filename, year=2015, day=18)

grid = [list(line) for line in raw.splitlines()]
R, C = len(grid), len(grid[0])


def step(n: int = 1, permanent: bool = False):
    for _ in range(n):
        turn_on = [] if not permanent else [(0, 0, "#"), (R - 1, 0, "#"), (0, C - 1, "#"), (R - 1, C - 1, "#")]
        for (r, c), v, _ in enumerate_grid(grid):
            on = sum(nv == "#" for _, nv in neighbours(grid, r, c, request=8))
            if v == "#" and 2 <= on <= 3:
                turn_on.append((r, c, "#"))
            elif v == "." and on == 3:
                turn_on.append((r, c, "#"))
        grid[:] = create_grid(R, C, blocks=turn_on)


step(100)
p1 = sum(v == "#" for _, v, _ in enumerate_grid(grid))
print(p1)

grid = [list(line) for line in raw.splitlines()]
grid[0][0] = "#"
grid[R - 1][0] = "#"
grid[0][C - 1] = "#"
grid[R - 1][C - 1] = "#"

step(100, True)
p2 = sum(v == "#" for _, v, _ in enumerate_grid(grid))
print(p2)

if args.test:
    args.tester(p1, p2)
