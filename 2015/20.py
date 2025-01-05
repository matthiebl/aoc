"""
--- Day 20: Infinite Elves and Infinite Houses ---
https://adventofcode.com/2015/day/20
"""

import numpy as np
from utils import *

args = parse_args(year=2015, day=20)
raw = get_input(args.filename, year=2015, day=20)

presents = int(raw)
houses = np.full(presents // 10, 10, dtype=int)
houses2 = np.full(presents // 10, 10, dtype=int)

for elf in range(2, presents // 10):
    houses[elf::elf] += elf * 10
    houses2[elf:50 * elf + 1:elf] += elf * 11

p1 = np.argmax(houses >= presents)
print(p1)
p2 = np.argmax(houses2 >= presents)
print(p2)

if args.test:
    args.tester(p1, p2)
