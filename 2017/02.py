"""
--- Day 2: Corruption Checksum ---
https://adventofcode.com/2017/day/2
"""

from utils import *

args = parse_args(year=2017, day=2)
raw = get_input(args.filename, year=2017, day=2)

rows = [tuple(nums(line)) for line in raw.splitlines()]

p1 = sum(max(row) - min(row) for row in rows)
print(p1)

p2 = sum(n // m for row in rows for n in row for m in row if n != m and n % m == 0)
print(p2)

if args.test:
    args.tester(p1, p2)
