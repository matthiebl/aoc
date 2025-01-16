"""
--- Day 23: Safe Cracking ---
https://adventofcode.com/2016/day/23
"""

from utils import *

args = parse_args(year=2016, day=23)
raw = get_input(args.filename, year=2016, day=23)

instructions = [line.split() for line in raw.splitlines()]


def is_multiply(instructions):
    return instructions == [
        ["cpy", "b", "c"],
        ["inc", "a"],
        ["dec", "c"],
        ["jnz", "c", "-2"],
        ["dec", "d"],
        ["jnz", "d", "-5"],
    ]


def program_output(instructions: list[list], a: int = 0, c: int = 0):
    registers = {"a": a, "b": 0, "c": c, "d": 0}
    ip = 0
    while ip < len(instructions):
        if is_multiply(instructions[ip:ip+6]):
            registers["a"] += registers["b"] * registers["d"]
            registers["c"] = 0
            registers["d"] = 0
            ip += 6
            continue

        [instruction, *parts] = instructions[ip]
        if instruction == "inc":
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
        elif instruction == "tgl":
            [x] = parts
            target = ip + registers[x] if x in registers else int(x)
            if 0 <= target < len(instructions):
                if len(instructions[target]) == 2:
                    instructions[target][0] = "dec" if instructions[target][0] == "inc" else "inc"
                else:
                    instructions[target][0] = "cpy" if instructions[target][0] == "jnz" else "jnz"
        ip += 1
    return registers["a"]


p1 = program_output([list(i) for i in instructions], a=7)
print(p1)

p2 = program_output([list(i) for i in instructions], a=12)
print(p2)

if args.test:
    args.tester(p1, p2)
