"""
--- Day 01: ... ---
https://adventofcode.com/2025/day/01
"""

from utils import *

args = parse_args(year=2025, day=1)
raw = get_input(args.filename, year=2025, day=1)

lines = raw.splitlines()

p1 = 0
p2 = 0

c = 50
for line in lines:
    d, n = line[0], int(line[1:])
    if n > 100:
        p2 += n // 100
        n %= 100

    if d == "R":
        if c != 0 and c + n >= 100:
            p2 += 1
        c += n
    elif d == "L":
        if c != 0 and c - n <= 0:
            p2 += 1
        c -= n
    c %= 100
    if c == 0:
        p1 += 1

print(p1)
print(p2)

if args.test:
    args.tester(p1, p2)
