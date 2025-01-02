"""
--- Day 6: Probably a Fire Hazard ---
https://adventofcode.com/2015/day/6

By using numpy's amazing array indexing, we can greatly speed up 2D array modifications.
https://numpy.org/doc/stable/user/basics.indexing.html#
"""

import numpy as np
from utils import *

args = parse_args(year=2015, day=6)
raw = get_input(args.filename, year=2015, day=6)

commands = raw.splitlines()

lights = np.zeros((1000, 1000), dtype=int)
brightness = np.zeros((1000, 1000), dtype=int)
for command in commands:
    r1, c1, r2, c2 = list(nums(command))
    sr, sc = slice(r1, r2 + 1), slice(c1, c2 + 1)
    match command[:7]:
        case "toggle ":
            lights[sr, sc] ^= 1
            brightness[sr, sc] += 2
        case "turn on":
            lights[sr, sc] = 1
            brightness[sr, sc] += 1
        case "turn of":
            lights[sr, sc] = 0
            brightness[sr, sc] -= 1
            brightness[brightness < 0] = 0

p1 = sum(sum(lights))
p2 = sum(sum(brightness))
print(p1)
print(p2)

if args.test:
    args.tester(p1, p2)
