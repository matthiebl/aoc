"""
--- Day 12: Subterranean Sustainability ---
https://adventofcode.com/2018/day/12
"""

from utils import *

args = parse_args(year=2018, day=12)
raw = get_input(args.filename, year=2018, day=12)

[initial], transforms = [group.splitlines() for group in raw.split("\n\n")]

transformations = {tuple(p == "#" for p in pots): to == "#" for pots, to in [t.split(" => ") for t in transforms]}
pots = set(i for i, pot in enumerate(initial.split(": ")[1]) if pot == "#")
min_pot, max_pot = min(pots), max(pots)

for gen in range(1000):
    sum_a = sum(pots)
    if gen == 20:
        p1 = sum_a
    pots = set(pot for pot in range(min_pot - 2, max_pot + 3)
               if transformations[tuple((pot + oth) in pots for oth in range(-2, 3))])
    min_pot, max_pot = min(pots), max(pots)
    sum_b = sum(pots)

print(p1)

p2 = sum_b + (50000000000 - 1000) * (sum_b - sum_a)
print(p2)

if args.test:
    args.tester(p1, p2)
