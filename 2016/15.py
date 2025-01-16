"""
--- Day 15: Timing is Everything ---
https://adventofcode.com/2016/day/15
"""

from utils import *

args = parse_args(year=2016, day=15)
raw = get_input(args.filename, year=2016, day=15)

discs = [(pos, slots) for _, slots, _, pos in [tuple(nums(line)) for line in raw.splitlines()]]


def time_until_fall(discs: list[tuple]):
    pos = [-p - i for i, (p, _) in enumerate(discs, 1)]
    sizes = [slots for _, slots in discs]
    return crt(pos, sizes)


p1 = time_until_fall(discs)
print(p1)

p2 = time_until_fall(discs + [(0, 11)])
print(p2)

if args.test:
    args.tester(p1, p2)
