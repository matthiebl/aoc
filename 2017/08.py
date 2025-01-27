"""
--- Day 8: I Heard You Like Registers ---
https://adventofcode.com/2017/day/8
"""

from collections import defaultdict

from utils import *

args = parse_args(year=2017, day=8)
raw = get_input(args.filename, year=2017, day=8)

cmps = {
    "<": lambda x, y: x < y,
    ">": lambda x, y: x > y,
    "<=": lambda x, y: x <= y,
    ">=": lambda x, y: x >= y,
    "==": lambda x, y: x == y,
    "!=": lambda x, y: x != y,
}

registers = defaultdict(int)


def value(s: str) -> int:
    if s.isnumeric() or s[0] == "-":
        return int(s)
    return registers[s]


instructions = raw.splitlines()
p2 = 0
for instruction in instructions:
    reg, change, amt, _, x, cmp, y = instruction.split()
    if cmps[cmp](value(x), value(y)):
        registers[reg] += (-1 if change == "dec" else 1) * value(amt)
    p2 = max(p2, *registers.values())

p1 = max(registers.values())
print(p1)
print(p2)

if args.test:
    args.tester(p1, p2)
