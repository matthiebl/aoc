"""
--- Day 24: Crossed Wires ---
https://adventofcode.com/2024/day/24
"""

from functools import cache
from itertools import combinations
from random import randint
from utils import *

args = parse_args(year=2024, day=24)
raw = get_input(args.filename, year=2024, day=24)

initial, connections = [group.splitlines() for group in raw.split("\n\n")]

values = {}
for line in initial:
    wire, value = line.split(": ")
    values[wire] = int(value)

wires = {}
for wire in connections:
    x, op, y, z = wire.replace(" -> ", " ").split(" ")
    wires[z] = (op, x, y)

operators = {
    "OR": lambda x, y: x | y,
    "XOR": lambda x, y: x ^ y,
    "AND": lambda x, y: x & y,
}


def eval(wire):
    if wire in values:
        return values[wire]

    op, x, y = wires[wire]
    return operators[op](eval(x), eval(y))


p1 = int("".join(map(str, [eval(f"z{i:02d}") for i in range(46)]))[::-1], 2)
print(p1)


def run(m: int = 45):
    bits = []
    for wire in wires:
        if wire[0] == "z":
            if int(wire[1:]) > m:
                continue
            bits.append((wire, eval(wire)))
    return "".join(map(str, [b for _, b in sorted(bits, reverse=True)]))


def test_sum(tests: int = 5):
    saved = values.copy()
    bad = False
    for _ in range(tests):
        x = "".join(["1" if randint(0, 1) == 1 else "0" for _ in range(45)])
        y = "".join(["1" if randint(0, 1) == 1 else "0" for _ in range(45)])
        for i in range(45):
            values[f"x{i:02d}"] = int(x[i])
            values[f"y{i:02d}"] = int(y[i])
        r = run()
        z = bin(int(x[::-1], 2) + int(y[::-1], 2))[2:].rjust(46, "0")
        if r != z:
            bad = True
    for s in saved:
        values[s] = saved[s]
    return not bad


x = "".join(map(str, [values[v] for v in sorted(values, reverse=True) if v[0] == "x"]))
y = "".join(map(str, [values[v] for v in sorted(values, reverse=True) if v[0] == "y"]))
z_target = bin(int(x, 2) + int(y, 2))[2:][::-1]

good = []


@cache
def is_solvable(bits: int, swaps: tuple):
    if bits == len(z_target):
        if len(swaps) != 8:
            return False
        if test_sum():
            good.append(swaps)
        return False
    try:
        up_to = run(bits)[::-1]
    except RecursionError:
        return False
    if up_to == z_target[:len(up_to)]:
        return is_solvable(bits + 1, swaps)
    if len(swaps) >= 8:
        return False
    for (a, b) in combinations(wires, 2):
        a, b = sorted((a, b))
        if a in swaps or b in swaps or (a[0] == "z" and b[0] == "z"):
            continue
        wires[a], wires[b] = wires[b], wires[a]
        try:
            up_to_2 = run(bits)[::-1]
        except RecursionError:
            wires[a], wires[b] = wires[b], wires[a]
            continue
        if up_to_2 == z_target[:len(up_to_2)] and is_solvable(bits + 1, tuple(s for s in swaps) + (a, b)):
            return True
        wires[a], wires[b] = wires[b], wires[a]
    return False


wires["vwr"], wires["z06"] = wires["z06"], wires["vwr"]
wires["tqm"], wires["z11"] = wires["z11"], wires["tqm"]
wires["kfs"], wires["z16"] = wires["z16"], wires["kfs"]
is_solvable(16, ("vwr", "z06", "tqm", "z11", "kfs", "z16"))

p2 = next(map(lambda t: ",".join(sorted(t)), good))
print(p2)

if args.test:
    args.tester(p1, p2)
