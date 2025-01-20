"""
--- Day 6: Signals and Noise ---
https://adventofcode.com/2016/day/6
"""

from collections import Counter

from utils import *

args = parse_args(year=2016, day=6)
raw = get_input(args.filename, year=2016, day=6)

lines = raw.splitlines()

p1 = ""
p2 = ""

for col in zip(*lines):
    freq = sorted((c, x) for x, c in Counter(col).items())
    p1 += freq[-1][1]
    p2 += freq[0][1]

print(p1)
print(p2)

if args.test:
    args.tester(p1, p2)
