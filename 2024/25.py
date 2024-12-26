"""
--- Day 25: Code Chronicle ---
https://adventofcode.com/2024/day/25
"""

from utils import *

args = parse_args(year=2024, day=25)
raw = get_input(args.filename, year=2024, day=25)

groups = [group.splitlines() for group in raw.split("\n\n")]

keys = []
locks = []

for block in groups:
    is_key = False
    if block[0] != "#####":
        is_key = True
    heights = tuple(r.count("#") - 1 for r in zip(*block))
    if is_key:
        keys.append(heights)
    else:
        locks.append(heights)

p1 = sum(all(l + k <= 5 for l, k in zip(lock, key)) for key in keys for lock in locks)
print(p1)

p2 = None
print(p2)

if args.test:
    args.tester(p1, p2)
