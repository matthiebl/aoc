"""
--- Day 1: Chronal Calibration ---
https://adventofcode.com/2018/day/1
"""

from utils import *

args = parse_args(year=2018, day=1)
raw = get_input(args.filename, year=2018, day=1)

frequencies = list(nums(raw))
p1 = sum(frequencies)
print(p1)

seen = set()
p2 = 0
i = 0
while p2 not in seen:
    seen.add(p2)
    p2 += frequencies[i]
    i = (i + 1) % len(frequencies)
print(p2)

if args.test:
    args.tester(p1, p2)
