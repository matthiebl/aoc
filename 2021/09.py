"""
--- Day 9: Smoke Basin ---
https://adventofcode.com/2021/day/9
"""

from utils import *

args = parse_args(year=2021, day=9)
raw = get_input(args.filename, year=2021, day=9)

grid = [list(line) for line in raw.splitlines()]

low_points = [(r, c) for (r, c), v, _ in enumerate_grid(grid) if all(nv > v for _, nv in neighbours(grid, r, c))]

p1 = sum(int(grid[r][c]) + 1 for r, c in low_points)
print(p1)

sizes = []
for point in low_points:
    stack = [point]
    seen = {point}
    while stack:
        r, c = stack.pop()
        for (nr, nc), v in neighbours(grid, r, c):
            if v != "9" and (nr, nc) not in seen:
                stack.append((nr, nc))
                seen.add((nr, nc))
    sizes.append(len(seen))

p2 = mul(sorted(sizes)[-3:])
print(p2)

if args.test:
    args.tester(p1, p2)
