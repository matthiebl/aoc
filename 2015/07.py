"""
--- Day 7: Some Assembly Required ---
https://adventofcode.com/2015/day/7
"""

from functools import cache
from re import search
from utils import *

args = parse_args(year=2015, day=7)
raw = get_input(args.filename, year=2015, day=7)

wires = {k: v for v, k in [line.split(" -> ") for line in raw.splitlines()]}


@cache
def compute(wire: str) -> int:
    if wire.isnumeric():
        return int(wire)
    gate = wires[wire]
    if gate.isnumeric():
        return int(gate)
    if len(gate) <= 2:
        return compute(gate)
    if gate.startswith("NOT"):
        return (2 ** 17 - 1) ^ compute(gate[4:])
    x, op, y = search(r"(\w+) (\w+) (\w+)", gate).groups()
    if op == "OR":
        return compute(x) | compute(y)
    if op == "AND":
        return compute(x) & compute(y)
    if op == "LSHIFT":
        return compute(x) << compute(y)
    if op == "RSHIFT":
        return compute(x) >> compute(y)


p1 = compute("a")
print(p1)

compute.cache_clear()
wires["b"] = str(p1)
p2 = compute("a")
print(p2)

if args.test:
    args.tester(p1, p2)
