"""
--- Day 1: Sonar Sweep ---
https://adventofcode.com/2021/day/1
"""

from utils import *

args = parse_args(year=2021, day=1)
raw = get_input(args.filename, year=2021, day=1)

depths = list(nums(raw))

p1 = sum(b > a for a, b in windows(depths))
print(p1)

p2 = sum(d > a for a, _, _, d in windows(depths, n=4))
print(p2)

if args.test:
    args.tester(p1, p2)
