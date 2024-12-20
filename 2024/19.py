"""
--- Day 19: Linen Layout ---
https://adventofcode.com/2024/day/19
"""

from functools import cache
from utils import *

args = parse_args(year=2024, day=19)
raw = get_input(args.filename, year=2024, day=19)

towels, targets = [group.splitlines() for group in raw.split("\n\n")]
towels = set(towels[0].split(", "))

p1 = 0
p2 = 0

@cache
def make(target: str) -> bool:
    if len(target) == 0:
        return 1
    return sum(make(target[len(towel):]) for towel in towels if target.startswith(towel))

for target in targets:
    p1 += 1 if make(target) else 0
    p2 += make(target)

print(p1)
print(p2)

if args.test:
    args.tester(p1, p2)
