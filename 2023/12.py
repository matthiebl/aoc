"""
--- Day 12: Hot Springs ---
https://adventofcode.com/2023/day/12
"""

from functools import cache
from utils import *

args = parse_args(year=2023, day=12)
raw = get_input(args.filename, year=2023, day=12)

lines = list(map(lambda l: (l[:l.index(" ")], tuple(nums(l))), raw.splitlines()))


@cache
def try_options(mask: str, nums: tuple[int]):
    if len(nums) == 0:
        return 1 if mask.count('#') == 0 else 0

    first = nums[0]
    rest = nums[1:]
    to_leave = sum(rest) + len(rest)

    total = 0
    for dots in range(len(mask) - to_leave - first + 1):
        s = '.' * dots + '#' * first + '.'
        if not all(m == o or m == '?' for m, o in zip(mask, s)):
            continue
        total += try_options(mask[len(s):], rest)

    return total


p1 = sum(try_options(springs, tuple(sizes)) for springs, sizes in lines)
print(p1)

p2 = sum(try_options("?".join([springs] * 5), tuple(sizes) * 5) for springs, sizes in lines)
print(p2)

if args.test:
    args.tester(p1, p2)
