"""
--- Day 16: The Floor Will Be Lava ---
https://adventofcode.com/2023/day/16
"""

from collections import deque
from utils import *


args = parse_args(year=2023, day=16)
raw = get_input(args.filename, year=2023, day=16)

grid = [list(line) for line in raw.splitlines()]
R, C = len(grid), len(grid[0])

p1 = 0
p2 = 0

D = [(0, 1), (1, 0), (0, -1), (-1, 0)]
ND = {
    "/":  {0: 3, 1: 2, 2: 1, 3: 0},
    "\\": {0: 1, 1: 0, 2: 3, 3: 2},
}


def shine_beam(r: int, c: int, d: int) -> set:
    visited = set()
    queue = deque([(r, c, d)])
    while queue:
        r, c, d = queue.popleft()
        if (r, c, d) in visited:
            continue
        visited.add((r, c, d))
        dr, dc = D[d]
        r, c = r + dr, c + dc
        while within_grid(grid, r, c) and (d % 2 == 0 and grid[r][c] in ".-" or d % 2 == 1 and grid[r][c] in ".|"):
            visited.add((r, c, d))
            r, c = r + dr, c + dc
        if not within_grid(grid, r, c):
            continue
        if grid[r][c] in ["/", "\\"]:
            queue.append((r, c, ND[grid[r][c]][d]))
        elif grid[r][c] == "-":
            queue.append((r, c, 0))
            queue.append((r, c, 2))
        elif grid[r][c] == "|":
            queue.append((r, c, 1))
            queue.append((r, c, 3))
    return len(set([(r, c) for r, c, _ in visited])) - 1


p1 = shine_beam(0, -1, 0)
print(p1)

p2 = max(*[shine_beam(r, -1, 0) for r in range(R)], *[shine_beam(-1, c, 1) for c in range(C)],
         *[shine_beam(r, C, 2) for r in range(R)], *[shine_beam(R, c, 3) for c in range(C)])
print(p2)

if args.test:
    args.tester(p1, p2)
