"""
--- Day 3: No Matter How You Slice It ---
https://adventofcode.com/2018/day/3
"""

from collections import defaultdict

from utils import *

args = parse_args(year=2018, day=3)
raw = get_input(args.filename, year=2018, day=3)

claims = defaultdict(set)
rectangles = [tuple(nums(line)) for line in raw.splitlines()]
for (id_, xi, yi, w, h) in rectangles:
    for x in range(xi, xi + w):
        for y in range(yi, yi + h):
            claims[x, y].add(id_)

p1 = sum(len(ids) >= 2 for ids in claims.values())
print(p1)

ids = set(id_ for id_, _, _, _, _ in rectangles)
for claim_ids in claims.values():
    if len(claim_ids) >= 2:
        ids -= claim_ids
p2 = ids.pop()
print(p2)

if args.test:
    args.tester(p1, p2)
