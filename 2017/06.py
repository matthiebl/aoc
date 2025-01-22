"""
--- Day 6: Memory Reallocation ---
https://adventofcode.com/2017/day/6
"""

from utils import *

args = parse_args(year=2017, day=6)
raw = get_input(args.filename, year=2017, day=6)

banks = list(nums(raw))


def cycle():
    m = max(banks)
    i = banks.index(m)
    banks[i] = 0
    while m:
        i += 1
        banks[i % len(banks)] += 1
        m -= 1


p1 = 0
states = set()
while tuple(banks) not in states:
    states.add(tuple(banks))
    cycle()
    p1 += 1
print(p1)

p2 = 1
state = tuple(banks)
cycle()
while tuple(banks) != state:
    cycle()
    p2 += 1
print(p2)

if args.test:
    args.tester(p1, p2)
