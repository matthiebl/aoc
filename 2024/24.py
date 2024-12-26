"""
--- Day 24: Crossed Wires ---
https://adventofcode.com/2024/day/24
"""

from collections import defaultdict
from utils import *

args = parse_args(year=2024, day=24)
raw = get_input(args.filename, year=2024, day=24)

initial, connections = [group.splitlines() for group in raw.split("\n\n")]

values = {}
for line in initial:
    wire, value = line.split(": ")
    values[wire] = int(value)

wires = {}
used_by = defaultdict(list)
for wire in connections:
    x, op, y, z = wire.replace(" -> ", " ").split(" ")
    wires[z] = (op, *sorted((x, y)))
    used_by[x].append(z)
    used_by[y].append(z)

for u in used_by:
    used_by[u].sort()


def eval(wire):
    if wire in values:
        return values[wire]
    operators = {
        "OR": lambda x, y: x | y,
        "XOR": lambda x, y: x ^ y,
        "AND": lambda x, y: x & y,
    }
    op, x, y = wires[wire]
    return operators[op](eval(x), eval(y))


p1 = int("".join(map(str, [eval(f"z{i:02d}") for i in range(46)]))[::-1], 2)
print(p1)


def check_input_xor(wire: str) -> bool:
    if wire == "z00":
        return True
    # should have one XOR and one AND, and at most one "z"
    users = used_by[wire]
    if len(users) != 2:
        return False
    a, b = users
    a_op, _, _ = wires[a]
    b_op, _, _ = wires[b]
    return a[0] != "z" and (a_op == "XOR" or b_op == "XOR") and (a_op == "AND" or b_op == "AND")


def check_and(wire: str) -> bool:
    if wires[wire][1] == "x00":
        return True
    users = used_by[wire]
    if len(users) != 1:
        return False
    op, _, _ = wires[users[0]]
    return op == "OR"


incorrect = []
for z, (op, x, y) in wires.items():
    if op == "XOR":
        if x[0] == "x" and y[0] == "y":
            if not check_input_xor(z):
                incorrect.append(z)
        elif not z[0] == "z":
            # output z XOR
            incorrect.append(z)
    elif op == "AND":
        if not check_and(z):
            incorrect.append(z)
    elif len(used_by[z]) != 2 and z != "z45":
        # carry OR
        incorrect.append(z)

p2 = ",".join(sorted(incorrect))
print(p2)

if args.test:
    args.tester(p1, p2)
