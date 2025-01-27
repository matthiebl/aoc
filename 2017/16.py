"""
--- Day 16: Permutation Promenade ---
https://adventofcode.com/2017/day/16
"""

from utils import *

args = parse_args(year=2017, day=16)
raw = get_input(args.filename, year=2017, day=16)

moves = raw.split(",")
program = list("abcdefghijklmnop")


def dance():
    for move in moves:
        if move[0] == "s":
            (x,) = nums(move)
            program[:] = program[-x:] + program[:-x]
        elif move[0] == "x":
            a, b = nums(move)
            program[a], program[b] = program[b], program[a]
        else:
            a, b = move[1:].split("/")
            i, j = program.index(a), program.index(b)
            program[i], program[j] = program[j], program[i]
    return "".join(program)


p1 = dance()
print(p1)

t = 1
while t < 1_000_000_000:
    p2 = dance()
    t += 1
    if "".join(program) == "abcdefghijklmnop":
        t = 1_000_000_000 - (1_000_000_000 % t)
print(p2)

if args.test:
    args.tester(p1, p2)
