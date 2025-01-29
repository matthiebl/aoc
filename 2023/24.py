"""
--- Day 24: Never Tell Me The Odds ---
https://adventofcode.com/2023/day/24
"""

from sympy import solve, symbols

from utils import *

args = parse_args(year=2023, day=24)
raw = get_input(args.filename, year=2023, day=24)

hailstones = [tuple(nums(line)) for line in raw.splitlines()]


def line_line_intersection(x1, y1, x2, y2, x3, y3, x4, y4):
    det = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if det == 0:
        return None, None
    x = (x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)
    y = (x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)
    return x / det, y / det


MIN = 200000000000000
MAX = 400000000000000
p1 = 0
for i, (x1, y1, _, dx1, dy1, _) in enumerate(hailstones):
    for (x2, y2, _, dx2, dy2, _) in hailstones[i + 1:]:
        x, y = line_line_intersection(x1, y1, x1 + dx1, y1 + dy1, x2, y2, x2 + dx2, y2 + dy2)
        if (x is not None and y is not None
                and MIN <= x <= MAX and MIN <= y <= MAX
                and (x - x1) / dx1 >= 0 and (x - x2) / dx2 >= 0):
            p1 += 1
print(p1)

equations = []
rx, ry, rz, rdx, rdy, rdz = symbols('rx, ry, rz, rdx, rdy, rdz')
for x, y, z, dx, dy, dz in hailstones[:4]:
    equations.append((dy - rdy) * (rx - x) - (dx - rdx) * (ry - y))
    equations.append((dz - rdz) * (rx - x) - (dx - rdx) * (rz - z))

answers = solve(equations)[0]
p2 = sum([answers[rx], answers[ry], answers[rz]])
print(p2)

if args.test:
    args.tester(p1, p2)
