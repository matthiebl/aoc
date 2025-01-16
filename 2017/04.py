"""
--- Day 4: ... ---
https://adventofcode.com/2017/day/4
"""

from utils import *

args = parse_args(year=2017, day=4)
raw = get_input(args.filename, year=2017, day=4)

lines = [line.split() for line in raw.splitlines()]
p1 = sum(len(line) == len(set(line)) for line in lines)
print(p1)

lines = [list(map(lambda w: "".join(sorted(w)), line)) for line in lines]
p2 = sum(len(line) == len(set(line)) for line in lines)
print(p2)

if args.test:
    args.tester(p1, p2)
