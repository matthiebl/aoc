"""
--- Day 20: Firewall Rules ---
https://adventofcode.com/2016/day/20
"""

from utils import *

args = parse_args(year=2016, day=20)
raw = get_input(args.filename, year=2016, day=20)

blacklist = sorted(tuple(map(int, line.split("-"))) for line in raw.splitlines())

p1 = None
p2 = 0

_, last = blacklist[0]
for lo, hi in blacklist:
    if hi <= last:
        continue
    if lo > last + 1:
        if p1 is None:
            p1 = last + 1
        p2 += lo - (last + 1)
    last = hi

print(p1)
print(p2)

if args.test:
    args.tester(p1, p2)
