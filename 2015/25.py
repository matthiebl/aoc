"""
--- Day 25: Let It Snow ---
https://adventofcode.com/2015/day/25
"""

from utils import *

args = parse_args(year=2015, day=25)
raw = get_input(args.filename, year=2015, day=25)

R, C = nums(raw)

code = 20151125
r, c = 2, 1
while not (r == R and c == C):
    code = (code * 252533) % 33554393
    if r == 1:
        r = c + 1
        c = 1
    else:
        r -= 1
        c += 1

p1 = (code * 252533) % 33554393
print(p1)

p2 = None
print(p2)

if args.test:
    args.tester(p1, p2)
