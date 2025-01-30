"""
--- Day 21: Step Counter ---
https://adventofcode.com/2023/day/21
"""

from collections import deque

from utils import *

args = parse_args(year=2023, day=21)
raw = get_input(args.filename, year=2023, day=21)

grid = [list(line) for line in raw.splitlines()]
size = len(grid)

distances = {}


def bfs(start):
    distances.clear()
    queue = deque(start)
    while queue:
        d, plot = queue.popleft()
        if plot in distances:
            continue
        distances[plot] = d
        for n, v in neighbours(grid, *plot):
            if n not in distances and v != "#":
                queue.append((d + 1, n))


distance_to_edge = size // 2
bfs([(0, next(find_in_grid(grid, "S")))])

p1 = sum(v < distance_to_edge and v % 2 == 0 for v in distances.values())
print(p1)

odd_corners = sum(v > distance_to_edge and v % 2 == 1 for v in distances.values())
bfs([(0, (0, 0)), (0, (size - 1, size - 1)), (0, (0, size - 1)), (0, (size - 1, 0))])
even_corners = sum(v < distance_to_edge and v % 2 == 0 for v in distances.values())

n = (26501365 - distance_to_edge) // size
odd_tiles = (n + 1) ** 2
even_tiles = n ** 2

p2 = (odd_tiles * sum(v % 2 == 1 for v in distances.values())
      + even_tiles * sum(v % 2 == 0 for v in distances.values())
      + n * even_corners
      - (n + 1) * odd_corners)
print(p2)

if args.test:
    args.tester(p1, p2)
