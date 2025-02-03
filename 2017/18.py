"""
--- Day 18: Duet ---
https://adventofcode.com/2017/day/18
"""

from collections import defaultdict, deque

from utils import *

args = parse_args(year=2017, day=18)
raw = get_input(args.filename, year=2017, day=18)

instructions: list[list[str]] = list(map(str.split, raw.splitlines()))
registers = defaultdict(int)


def value(x: str, reg: dict = registers):
    return int(x) if x.isnumeric() or x[0] == "-" else reg[x]


i = 0
while 0 <= i < len(instructions):
    match instructions[i]:
        case ["snd", x]:
            p1 = value(x)
        case ["rcv", x]:
            if value(x) != 0:
                break
        case ["set", x, y]:
            registers[x] = value(y)
        case ["add", x, y]:
            registers[x] += value(y)
        case ["mul", x, y]:
            registers[x] *= value(y)
        case ["mod", x, y]:
            registers[x] %= value(y)
        case ["jgz", x, y]:
            if value(x) > 0:
                i += value(y) - 1
    i += 1

print(p1)

p2 = 0
registers0 = defaultdict(int)
registers1 = defaultdict(int)
registers1["p"] = 1
queue0 = deque()
queue1 = deque()
i0, i1 = 0, 0
while 0 <= i1 < len(instructions):
    while 0 <= i0 < len(instructions):
        if not queue0 and instructions[i0][0] == "rcv":
            break
        match instructions[i0]:
            case ["snd", x]:
                queue1.append(value(x, registers0))
            case ["rcv", x]:
                registers0[x] = queue0.popleft()
            case ["set", x, y]:
                registers0[x] = value(y, registers0)
            case ["add", x, y]:
                registers0[x] += value(y, registers0)
            case ["mul", x, y]:
                registers0[x] *= value(y, registers0)
            case ["mod", x, y]:
                registers0[x] %= value(y, registers0)
            case ["jgz", x, y]:
                if value(x, registers0) > 0:
                    i0 += value(y, registers0) - 1
        i0 += 1
    while 0 <= i1 < len(instructions):
        if not queue1 and instructions[i1][0] == "rcv":
            break
        match instructions[i1]:
            case ["snd", x]:
                queue0.append(value(x, registers1))
                p2 += 1
            case ["rcv", x]:
                registers1[x] = queue1.popleft()
            case ["set", x, y]:
                registers1[x] = value(y, registers1)
            case ["add", x, y]:
                registers1[x] += value(y, registers1)
            case ["mul", x, y]:
                registers1[x] *= value(y, registers1)
            case ["mod", x, y]:
                registers1[x] %= value(y, registers1)
            case ["jgz", x, y]:
                if value(x, registers1) > 0:
                    i1 += value(y, registers1) - 1
        i1 += 1
    if not queue0 and not queue1 and instructions[i0][0] == "rcv" and instructions[i1][0] == "rcv":
        break

print(p2)

if args.test:
    args.tester(p1, p2)
