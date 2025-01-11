"""
--- Day 3: Spiral Memory ---
https://adventofcode.com/2017/day/3
"""

from utils import *

args = parse_args(year=2017, day=3)
raw = get_input(args.filename, year=2017, day=3)

steps = int(raw)

#    L        D       R       U 
D = [(0, -1), (1, 0), (0, 1), (-1, 0)]

r, c = (0, 0)
spiral = {(r, c): 1}

moves = 1
d = 2
p2 = 0
while moves < steps:
    dr, dc = D[d % len(D)]
    for _ in range(d // 2):
        r, c = r + dr, c + dc
        if not p2:
            v = sum(spiral.get((r + ddr, c + ddc), 0) for ddr, ddc in directions(8))
            spiral[(r, c)] = v
            if v >= steps:
                p2 = v
    moves += d // 2
    d += 1
# Move back any overshoot
dr, dc = D[(d + 1) % len(D)]
r, c = r + dr * (moves - steps), c + dc * (moves - steps)

p1 = abs(r) + abs(c)
print(p1)

print(p2)

if args.test:
    args.tester(p1, p2)
