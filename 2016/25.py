"""
--- Day 25: Clock Signal ---
https://adventofcode.com/2016/day/25
"""

from utils import *

args = parse_args(year=2016, day=25)
raw = get_input(args.filename, year=2016, day=25)

instructions = [line.split() for line in raw.splitlines()]


def program_output(instructions: list[list], a: int = 0, c: int = 0):
    buffer = [2]
    registers = {"a": a, "b": 0, "c": c, "d": 0}
    ip = 0
    while ip < len(instructions):
        if len(buffer) > 100:
            return True
        [instruction, *parts] = instructions[ip]
        if instruction == "out":
            [x] = parts
            output = registers[x] if x in registers else int(x)
            if output not in [0, 1] or output == buffer[-1]:
                return False
            buffer.append(output)
        elif instruction == "inc":
            [x] = parts
            if x in registers:
                registers[x] += 1
        elif instruction == "dec":
            [x] = parts
            if x in registers:
                registers[x] -= 1
        elif instruction == "cpy":
            x, y = parts
            if y in registers:
                registers[y] = registers[x] if x in registers else int(x)
        elif instruction == "jnz":
            x, y = parts
            if (registers[x] if x in registers else int(x)) != 0:
                ip += registers[y] if y in registers else int(y)
                continue
        ip += 1
    return registers["a"]


p1 = 1
while not program_output([list(i) for i in instructions], a=p1):
    p1 += 1
print(p1)

p2 = None
print(p2)

if args.test:
    args.tester(p1, p2)
