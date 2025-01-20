"""
--- Day 23: Opening the Turing Lock ---
https://adventofcode.com/2015/day/23
"""

from utils import *

args = parse_args(year=2015, day=23)
raw = get_input(args.filename, year=2015, day=23)

instructions = raw.splitlines()


def run_program(a: int = 0):
    registers = {"a": a, "b": 0}
    ip = 0
    while ip < len(instructions):
        instruction = instructions[ip]
        rule = instruction[:3]
        reg = instruction[4]
        if rule == "hlf":
            registers[reg] //= 2
        elif rule == "tpl":
            registers[reg] *= 3
        elif rule == "inc":
            registers[reg] += 1
        elif rule == "jmp":
            ip += next(nums(instruction))
            continue
        elif rule == "jie" and registers[reg] % 2 == 0:
            ip += next(nums(instruction))
            continue
        elif rule == "jio" and registers[reg] == 1:
            ip += next(nums(instruction))
            continue
        ip += 1
    return registers["b"]


p1 = run_program()
print(p1)

p2 = run_program(a=1)
print(p2)

if args.test:
    args.tester(p1, p2)
