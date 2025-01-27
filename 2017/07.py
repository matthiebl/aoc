"""
--- Day 7: Recursive Circus ---
https://adventofcode.com/2017/day/7
"""

from collections import Counter
from functools import cache

from utils import *

args = parse_args(year=2017, day=7)
raw = get_input(args.filename, year=2017, day=7)

lines = raw.splitlines()

tree = {}
standing = set()
for line in lines:
    if " -> " not in line:
        line += " -> "
    program, above = line.split(" -> ")
    name, weight = program.split(" ")
    tree[name] = {"weight": next(nums(weight)), "next": above.split(", ") if above else []}
    standing.update(above.split(", "))

p1 = next(iter(set(tree) - standing))
print(p1)


@cache
def weight_of(node: str):
    return tree[node]["weight"] + sum(weight_of(n) for n in tree[node]["next"])


def balance(node: str) -> int | None:
    children = {n: weight_of(n) for n in tree[node]["next"]}
    freq = Counter(children.values())
    if len(freq) == 1:
        return

    [(tw, _), (uw, _)] = freq.most_common()
    unbalanced = next(n for n, w in children.items() if w == uw)
    res = balance(unbalanced)
    if res is None:
        return tree[unbalanced]["weight"] - abs(tw - uw)
    return res


p2 = balance(p1)
print(p2)

if args.test:
    args.tester(p1, p2)
