"""
--- Day 6: Chronal Coordinates ---
https://adventofcode.com/2018/day/6
"""

from collections import defaultdict

from utils import *

args = parse_args(year=2018, day=6)
raw = get_input(args.filename, year=2018, day=6)

coords = set(map(lambda x: tuple(x), chunks(nums(raw))))

xm, ym = min(x for x, _ in coords), min(y for _, y in coords)
xmm, ymm = max(x for x, _ in coords), max(y for _, y in coords)
edge = set()
dist = defaultdict(int)

p2 = 0
for x in range(xm - 10, xmm + 10):
    for y in range(ym - 10, ymm + 10):
        dists = sorted((manhattan(x, y, xc, yc), xc, yc) for xc, yc in coords)
        if sum(d for d, _, _ in dists) < 32:
            p2 += 1
        _, xc, yc = dists[0]
        if x in [xm - 10, xmm + 10 - 1] or y in [ym - 10, ymm + 10 - 1]:
            edge.add((xc, yc))
        if dists[0][0] == dists[1][0]:
            continue
        dist[xc, yc] += 1

p1 = max(closest for coord, closest in dist.items() if coord not in edge)
print(p1)

print(p2)

if args.test:
    args.tester(p1, p2)
