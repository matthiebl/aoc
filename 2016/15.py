"""
--- Day 15: Timing is Everything ---
https://adventofcode.com/2016/day/15
"""

from utils import *

args = parse_args(year=2016, day=15)
raw = get_input(args.filename, year=2016, day=15)

discs = [tuple(nums(line)) for line in raw.splitlines()]


def time_until_fall(discs: list[tuple]):
    t = 0
    while True:
        if all((p + t + i) % slots == 0 for i, (_, slots, _, p) in enumerate(discs, 1)):
            return t
        t += 1


p1 = time_until_fall(discs)
print(p1)

p2 = time_until_fall(discs + [(0, 11, 0, 0)])
print(p2)

if args.test:
    args.tester(p1, p2)
