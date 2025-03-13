"""
--- Day 7: The Treachery of Whales ---
https://adventofcode.com/2021/day/7
"""

from utils import *

args = parse_args(year=2021, day=7)
raw = get_input(args.filename, year=2021, day=7)

crabs = list(nums(raw))

p1 = float("inf")
p2 = float("inf")

for x in range(min(crabs), max(crabs) + 1):
    a, b = 0, 0
    for crab in crabs:
        n = abs(x - crab)
        a += n
        b += (n * (n + 1)) // 2
    p1 = min(p1, a)
    p2 = min(p2, b)

print(p1)
print(p2)

if args.test:
    args.tester(p1, p2)
