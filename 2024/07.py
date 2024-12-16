"""
--- Day 7: Bridge Repair ---
https://adventofcode.com/2024/day/7
"""

from utils import *

args = parse_args(year=2024, day=7)
raw = get_input(args.filename, year=2024, day=7)

equations = [list(nums(line)) for line in raw.splitlines()]


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


p1 = sum(target for [target, *ns] in equations if can_obtain(target, ns))
print(p1)

p2 = sum(target for [target, *ns] in equations if can_obtain(target, ns, p2=True))
print(p2)

if args.test:
    args.tester(p1, p2)
