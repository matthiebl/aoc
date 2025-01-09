"""
--- Day 18: Like a Rogue ---
https://adventofcode.com/2016/day/18
"""

from utils import *

args = parse_args(year=2016, day=18)
raw = get_input(args.filename, year=2016, day=18)

p1, p2 = 0, 0
prev_row = [c == "." for c in raw]
for i in range(400000):
    safe = sum(prev_row)
    if i < 40:
        p1 += safe
    p2 += safe
    prev_row = [l == r for l, _, r in windows([True] + prev_row + [True], n=3)]

print(p1)
print(p2)

if args.test:
    args.tester(p1, p2)
