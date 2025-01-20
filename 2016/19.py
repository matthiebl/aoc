"""
--- Day 19: An Elephant Named Joseph ---
https://adventofcode.com/2016/day/19
"""

from math import floor, log

from utils import *

args = parse_args(year=2016, day=19)
raw = get_input(args.filename, year=2016, day=19)

elves = int(raw)

a = floor(log(elves, 2))
p1 = 2 * (elves - 2 ** a) + 1
print(p1)

pow_3a = 3 ** floor(log(elves, 3))
p2 = elves - pow_3a + (elves - 2 * pow_3a if elves > 2 * pow_3a else 0)
print(p2)

if args.test:
    args.tester(p1, p2)
