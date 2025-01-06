"""
--- Day 8: Two-Factor Authentication ---
https://adventofcode.com/2016/day/8
"""

from utils import *

args = parse_args(year=2016, day=8)
raw = get_input(args.filename, year=2016, day=8)

instructions = raw.splitlines()

R, C = 6, 50
pixels = set()

for instruction in instructions:
    if "rect" in instruction:
        w, h = nums(instruction)
        for r in range(h):
            for c in range(w):
                pixels.add((r, c))
    elif "rotate row" in instruction:
        rr, n = nums(instruction)
        pixels = {(r, (c + n) % C if r == rr else c) for r, c in pixels}
    elif "rotate col" in instruction:
        cc, n = nums(instruction)
        pixels = {((r + n) % R if c == cc else r, c) for r, c in pixels}

p1 = len(pixels)
print(p1)

grid = create_grid(R, C, fill=" ", blocks=[(r, c, "\u2588") for r, c in pixels])
p2 = ["".join(r) for r in grid]
print("\n".join(p2))

if args.test:
    args.tester(p1, p2)
