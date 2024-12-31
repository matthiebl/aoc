"""
--- Day 14: Parabolic Reflector Dish ---
https://adventofcode.com/2023/day/14
"""

from utils import *

args = parse_args(year=2023, day=14)
raw = get_input(args.filename, year=2023, day=14)

grid = [list(line) for line in raw.splitlines()]


def rotate():
    grid[:] = list(zip(*grid[::-1]))


def slide_east():
    grid[:] = [list("#".join(["".join(sorted(s)) for s in "".join(row).split("#")])) for row in grid]


rotate()
slide_east()
p1 = sum(c + 1 for r, c in find_in_grid(grid, "O"))
print(p1)

grid = [list(line) for line in raw.splitlines()]
seen_states = {}
t = 0
while t < 10 ** 9:
    for _ in range(4):
        rotate()
        slide_east()
    state = tuple("".join(row) for row in grid)
    if state in seen_states:
        cycle = t - seen_states[state]
        t += cycle * ((10 ** 9 - t) // cycle)
    seen_states[state] = t
    t += 1

rotate()
p2 = sum(c + 1 for r, c in find_in_grid(grid, "O"))
print(p2)

if args.test:
    args.tester(p1, p2)
