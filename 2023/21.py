"""
--- Day 21: Step Counter ---
https://adventofcode.com/2023/day/21
"""

from utils import *

args = parse_args(year=2023, day=21)
raw = get_input(args.filename, year=2023, day=21)

grid = [list(line) for line in raw.splitlines()]
R, C = len(grid), len(grid[0])

plots = set([next(find_in_grid(grid, "S"))])


def step(n: int = 1):
    global plots
    if n == 0:
        return len(plots)
    reachable = set()
    for r, c in plots:
        for dr, dc in directions():
            nr, nc = r + dr, c + dc
            if grid[nr % R][nc % C] in ".S":
                reachable.add((nr, nc))
    plots = reachable
    return step(n - 1)


p1 = step(64)
print(p1)

sequence = [step(), step(131), step(131)]

for _ in range(26501365 // R - 2):
    reduced = [sequence[-3:]]
    while not all(n == 0 for n in reduced[-1]):
        reduced.append([m - n for n, m in windows(reduced[-1])])
    reduced[-1].append(0)
    sequence.append(sum(ns[-1] for ns in reduced))

p2 = sequence[-1]
print(p2)

if args.test:
    args.tester(p1, p2)
