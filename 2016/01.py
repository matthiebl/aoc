"""
--- Day 1: No Time for a Taxicab ---
https://adventofcode.com/2016/day/1
"""

from utils import *

args = parse_args(year=2016, day=1)
raw = get_input(args.filename, year=2016, day=1)

moves = raw.split(", ")
visited = set()

D = [(-1, 0), (0, 1), (1, 0), (0, -1)]

p2 = 0
r, c, d = 0, 0, 0
for move in moves:
    d += 1 if move[0] == "R" else -1
    (n,) = nums(move)
    dr, dc = D[d % len(D)]
    for _ in range(n):
        if (r, c) in visited and not p2:
            p2 = manhattan(r, c, 0, 0)
        visited.add((r, c))
        r, c = r + dr, c + dc

p1 = manhattan(r, c, 0, 0)
print(p1)
print(p2)

if args.test:
    args.tester(p1, p2)
