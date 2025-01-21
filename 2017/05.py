"""
--- Day 5: A Maze of Twisty Trampolines, All Alike ---
https://adventofcode.com/2017/day/5
"""

from utils import *

args = parse_args(year=2017, day=5)
raw = get_input(args.filename, year=2017, day=5)


def jumps(do_decrease: bool = False):
    instructions = list(nums(raw))
    index, steps, n = 0, 0, len(instructions)
    while 0 <= index < n:
        steps += 1
        if do_decrease and instructions[index] >= 3:
            instructions[index] -= 1
            index += instructions[index] + 1
        else:
            instructions[index] += 1
            index += instructions[index] - 1
    return steps


p1 = jumps()
print(p1)

p2 = jumps(do_decrease=True)
print(p2)

if args.test:
    args.tester(p1, p2)
