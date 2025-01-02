"""
--- Day 2: I Was Told There Would Be No Math ---
https://adventofcode.com/2015/day/2
"""

from utils import *

args = parse_args(year=2015, day=2)
raw = get_input(args.filename, year=2015, day=2)

presents = list(map(sorted, map(list, map(nums, raw.splitlines()))))

p1 = sum(3 * w * h + 2 * (w * d + h * d) for w, h, d in presents)
p2 = sum(2 * (w + h) + w * h * d for w, h, d in presents)
print(p1)
print(p2)

if args.test:
    args.tester(p1, p2)
