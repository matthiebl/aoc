"""
--- Day 2: Dive! ---
https://adventofcode.com/2021/day/2
"""

from utils import *

args = parse_args(year=2021, day=2)
raw = get_input(args.filename, year=2021, day=2)

instructions = raw.splitlines()

x, depth = 0, 0
for instruction in instructions:
    match instruction.split():
        case ["forward", n]:
            x += int(n)
        case ["up", n]:
            depth -= int(n)
        case ["down", n]:
            depth += int(n)

p1 = x * depth
print(p1)

x, depth, aim = 0, 0, 0
for instruction in instructions:
    match instruction.split():
        case ["forward", n]:
            x += int(n)
            depth += aim * int(n)
        case ["up", n]:
            aim -= int(n)
        case ["down", n]:
            aim += int(n)

p2 = x * depth
print(p2)

if args.test:
    args.tester(p1, p2)
