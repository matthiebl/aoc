"""
--- Day 17: No Such Thing as Too Much ---
https://adventofcode.com/2015/day/17
"""

from collections import defaultdict
from utils import *

args = parse_args(year=2015, day=17)
raw = get_input(args.filename, year=2015, day=17)

containers = list(nums(raw))
size = defaultdict(int)


def container_combinations(total: int = 0, target: int = 150, taken: int = 0, i: int = 0) -> int:
    if i == len(containers):
        if total == target:
            size[taken] += 1
        return 1 if total == target else 0
    return (container_combinations(total + containers[i], target, taken + 1, i + 1)
            + container_combinations(total, target, taken, i + 1))


p1 = container_combinations()
print(p1)

p2 = size[sorted(size)[0]]
print(p2)

if args.test:
    args.tester(p1, p2)
