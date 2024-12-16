"""
--- Day 5: Print Queue ---
https://adventofcode.com/2024/day/5
"""

from functools import cmp_to_key
from utils import *

args = parse_args(year=2024, day=5)
raw = get_input(args.filename, year=2024, day=5)

groups = [group.splitlines() for group in raw.split("\n\n")]

rules, updates = [[tuple(nums(line)) for line in group] for group in groups]


def rules_pass(update: tuple):
    for ra, rb in rules:
        if ra in update and rb in update and update.index(ra) >= update.index(rb):
            return False
    return True


def compare(a: int, b: int) -> int:
    return -1 if (a, b) in rules else 1


p1 = 0
p2 = 0
for update in updates:
    if rules_pass(update):
        p1 += update[len(update) // 2]
        continue
    ordered = sorted(update, key=cmp_to_key(compare))
    p2 += ordered[len(ordered) // 2]

print(p1)
print(p2)

if args.test:
    args.tester(p1, p2)
