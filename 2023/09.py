"""
--- Day 9: Mirage Maintenance ---
https://adventofcode.com/2023/day/9
"""

from functools import reduce
from utils import *

args = parse_args(year=2023, day=9)
raw = get_input(args.filename, year=2023, day=9)

sequences = []
for line in raw.splitlines():
    ns = [list(nums(line))]
    while not all(n == 0 for n in ns[-1]):
        ns.append([m - n for n, m in windows(ns[-1])])
    sequences.append(ns)

p1 = 0
p2 = 0
for sequence in sequences:
    p1 += sum(ns[-1] for ns in sequence)
    p2 += reduce(lambda cur, nxt: nxt - cur, [ns[0] for ns in sequence][::-1], 0)
print(p1)
print(p2)

if args.test:
    args.tester(p1, p2)
