"""
--- Day 19: An Elephant Named Joseph ---
https://adventofcode.com/2016/day/19
"""

from math import floor, log2
from utils import *

args = parse_args(year=2016, day=19)
raw = get_input(args.filename, year=2016, day=19)

target = int(raw)

a = floor(log2(target))
p1 = 2 * (target - 2 ** a) + 1
print(p1)

elves = list(range(target))
presents = {elf: 1 for elf in elves}

while len(elves) > 1:
    i = 0
    while i < len(elves):
        elf = elves[i]
        if elf in presents:
            target_i = (i + len(elves) // 2) % len(elves)
            target_elf = elves[target_i]
            presents[elf] += presents[target_elf]
            del presents[target_elf]
            elves.pop(target_i)
            if target_i > i:
                i += 1
        else:
            elves.pop(i)

p2 = elves.pop() + 1
print(p2)

if args.test:
    args.tester(p1, p2)
