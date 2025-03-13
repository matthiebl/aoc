"""
--- Day 5: Hydrothermal Venture ---
https://adventofcode.com/2021/day/5
"""

from collections import defaultdict

from utils import *

args = parse_args(year=2021, day=5)
raw = get_input(args.filename, year=2021, day=5)

lines = [tuple(nums(line)) for line in raw.splitlines()]

points = defaultdict(int)
points2 = defaultdict(int)

for x1, y1, x2, y2 in lines:
    (x1, y1), (x2, y2) = sorted([(x1, y1), (x2, y2)])
    if x1 == x2 or y1 == y2:
        for xx in range(x1, x2 + 1):
            for yy in range(y1, y2 + 1):
                points[(xx, yy)] += 1
                points2[(xx, yy)] += 1
    else:
        dx, dy = (1, -1) if y2 < y1 else (1, 1)
        xx, yy = x1, y1
        points2[(xx, yy)] += 1
        while (xx, yy) != (x2, y2):
            xx += dx
            yy += dy
            points2[(xx, yy)] += 1

p1 = sum(v > 1 for v in points.values())
print(p1)

p2 = sum(v > 1 for v in points2.values())
print(p2)

if args.test:
    args.tester(p1, p2)
