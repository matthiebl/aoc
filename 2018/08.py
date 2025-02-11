"""
--- Day 8: Memory Maneuver ---
https://adventofcode.com/2018/day/8
"""

from utils import *

args = parse_args(year=2018, day=8)
raw = get_input(args.filename, year=2018, day=8)

tree = list(nums(raw))[::-1]


def metadata():
    children, meta = tree.pop(), tree.pop()
    total = sum(metadata() for _ in range(children)) if children else 0
    total += sum(tree.pop() for _ in range(meta))
    return total


p1 = metadata()
print(p1)

tree = list(nums(raw))[::-1]


def value():
    children, meta = tree.pop(), tree.pop()
    values = {i: v for i, v in enumerate((value() for _ in range(children)), start=1)}
    if not children:
        return sum(tree.pop() for _ in range(meta))
    return sum(values.get(tree.pop(), 0) for _ in range(meta))


p2 = value()
print(p2)

if args.test:
    args.tester(p1, p2)
