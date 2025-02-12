"""
--- Day 11: Chronal Charge ---
https://adventofcode.com/2018/day/11
"""

import numpy as np

from utils import *

args = parse_args(year=2018, day=11)
serial = int(get_input(args.filename, year=2018, day=11))

grid = np.empty(shape=(300, 300))
for x in range(1, 301):
    for y in range(1, 301):
        rack_id = x + 10
        grid[x-1, y-1] = ((rack_id * y + serial) * rack_id % 1000) // 100 - 5

p1, p1_power = "", 0
p2, p2_power = "", 0
for size in range(2, 33):
    for x in range(1, 301 - size + 1):
        for y in range(1, 301 - size + 1):
            power = grid[x-1:x-1+size, y-1:y-1+size].sum()
            if size == 3 and power > p1_power:
                p1 = f"{x},{y}"
                p1_power = power
            if power > p2_power:
                p2 = f"{x},{y},{size}"
                p2_power = power
print(p1)
print(p2)

if args.test:
    args.tester(p1, p2)
