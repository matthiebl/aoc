"""
--- Day 8: Matchsticks ---
https://adventofcode.com/2015/day/8
"""

from utils import *

args = parse_args(year=2015, day=8)
raw = get_input(args.filename, year=2015, day=8)

strings = raw.splitlines()

p1 = sum(len(s) - len(s.encode().decode("unicode-escape")) + 2 for s in strings)
print(p1)

p2 = sum(len(repr(s)) - len(s) + s.count('"') for s in strings)
print(p2)

if args.test:
    args.tester(p1, p2)
