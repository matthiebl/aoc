"""
--- Day 12: Leonardo's Monorail ---
https://adventofcode.com/2016/day/12
"""

from utils import *

args = parse_args(year=2016, day=12)
raw = get_input(args.filename, year=2016, day=12)

instructions = [line.split() for line in raw.splitlines()]


def program_output(c: int = 0):
    registers = {"a": 0, "b": 0, "c": c, "d": 0}
    ip = 0
    while ip < len(instructions):
        [instruction, *parts] = instructions[ip]
        if instruction == "cpy":
            x, y = parts
            registers[y] = registers[x] if x in "abcd" else int(x)
        elif instruction == "inc":
            [x] = parts
            registers[x] += 1
        elif instruction == "dec":
            [x] = parts
            registers[x] -= 1
        elif instruction == "jnz":
            x, y = parts
            if (registers[x] if x in "abcd" else int(x)) != 0:
                ip += int(y)
                continue
        ip += 1
    return registers["a"]


p1 = program_output()
print(p1)
p2 = program_output(c=1)
print(p2)

if args.test:
    args.tester(p1, p2)
