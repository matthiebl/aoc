"""
--- Day 8: Resonant Collinearity ---
https://adventofcode.com/2024/day/8
"""

from collections import defaultdict
from utils import *

args = parse_args(year=2024, day=8)
raw = get_input(args.filename, year=2024, day=8)

grid = [list(line) for line in raw.splitlines()]
R, C = len(grid), len(grid[0])

antennas = defaultdict(list)
for pos, freq, _ in enumerate_grid(grid):
    if freq != ".":
        antennas[freq].append(pos)

single_antinodes = set()
antinodes = set()
for freq in antennas:
    for i, (r1, c1) in enumerate(antennas[freq]):
        for (r2, c2) in antennas[freq][i+1:]:
            dr, dc = r2 - r1, c2 - c1
            single_antinodes.add((r1 - dr, c1 - dc))
            single_antinodes.add((r2 + dr, c2 + dc))

            ir, ic = r1, c1
            while 0 <= ir < R and 0 <= ic < C:
                antinodes.add((ir, ic))
                ir, ic = ir + dr, ic + dc
            ir, ic = r1, c1
            while 0 <= ir < R and 0 <= ic < C:
                antinodes.add((ir, ic))
                ir, ic = ir - dr, ic - dc

p1 = sum(1 for r, c in single_antinodes if within_grid(grid, r, c))
print(p1)

p2 = len(antinodes)
print(p2)

if args.test:
    args.tester(p1, p2)
