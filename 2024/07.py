#!/usr/bin/env python3.13

from sys import argv

from maoc import fetch, submit
from maoc.utils.parse import ints

"""
--- Day 7: Bridge Repair ---

https://adventofcode.com/2024/day/7
"""

print("Day 07")
FILE_NAME = argv[1] if len(argv) >= 2 else "07.in"
raw = fetch(year=2024, day=7, path=__file__, file_name=FILE_NAME)


def parse_raw():
    return [list(ints(line)) for line in raw.splitlines()]


equations = parse_raw()


def can_obtain(target: int, ns: list[int], p2=False):
    n = ns[-1]
    if len(ns) == 1:
        return target == n
    if target > n and can_obtain(target - n, ns[:-1], p2):
        return True
    if target % n == 0 and can_obtain(target // n, ns[:-1], p2):
        return True
    s_t = str(target)
    s_n = str(n)
    if p2 and len(s_t) > len(s_n) and s_t.endswith(s_n) and can_obtain(int(s_t[:-len(s_n)]), ns[:-1], p2):
        return True
    return False


def part_one():
    return sum(target for [target, *ns] in equations if can_obtain(target, ns))


def part_two():
    return sum(target for [target, *ns] in equations if can_obtain(target, ns, p2=True))


submit(year=2024, day=7, part=1, solution=part_one)
submit(year=2024, day=7, part=2, solution=part_two)
