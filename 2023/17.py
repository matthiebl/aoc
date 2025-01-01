"""
--- Day 17: Clumsy Crucible ---
https://adventofcode.com/2023/day/17
"""

from utils import *

args = parse_args(year=2023, day=17)
raw = get_input(args.filename, year=2023, day=17)

grid = [list(line) for line in raw.splitlines()]
R, C = len(grid), len(grid[0])


def dijkstras(min_steps: int = 1, max_steps: int = 3) -> tuple[int | None, dict]:
    from heapq import heappush, heappop
    from collections import defaultdict
    distances = defaultdict(lambda: float("inf"))
    distances[(0, 0, 0, 0, 0)] = 0

    heap = [(0, (0, 0), (0, 0), 0)]
    while heap:
        heat, (r, c), (dr, dc), steps = heappop(heap)
        if (r, c) == (R - 1, C - 1):
            return heat

        for ndr, ndc in directions(4):
            if (((dr, dc) == (ndr, ndc) and steps >= max_steps)
                    or ((dr, dc) not in [(0, 0), (ndr, ndc)] and steps < min_steps)
                    or ((dr, dc) == (-ndr, -ndc))
                    or (not within_grid(grid, r + ndr, c + ndc))):
                continue
            tentative = heat + int(grid[r + ndr][c + ndc])
            new_steps = steps + 1 if (dr, dc) == (ndr, ndc) else 1
            if tentative < distances[(r + ndr, c + ndc, ndr, ndc, new_steps)]:
                distances[(r + ndr, c + ndc, ndr, ndc, new_steps)] = tentative
                heappush(heap, (tentative, (r + ndr, c + ndc), (ndr, ndc), new_steps))


p1 = dijkstras()
print(p1)
p2 = dijkstras(min_steps=4, max_steps=10)
print(p2)

if args.test:
    args.tester(p1, p2)
