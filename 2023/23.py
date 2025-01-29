"""
--- Day 23: A Long Walk ---
https://adventofcode.com/2023/day/23
"""

from collections import deque

from utils import *

args = parse_args(year=2023, day=23)
raw = get_input(args.filename, year=2023, day=23)

grid = [list(line) for line in raw.splitlines()]
R, C = len(grid), len(grid[0])
start = (0, 1)
end = (R - 1, C - 2)

directional = {">": (0, 1), "v": (1, 0), "<": (0, -1), "^": (-1, 0)}

intersections = set([start, end])
for (r, c), v, _ in enumerate_grid(grid, skip="#"):
    if len([n for _, n in neighbours(grid, r, c) if n != "#"]) > 2:
        intersections.add((r, c))

directional_graph = {n: [] for n in intersections}
graph = {n: [] for n in intersections}


def intersection_search(pos: tuple):
    visited = set()
    queue = deque([(0, pos, False)])
    while queue:
        d, (r, c), climbed = queue.popleft()
        if (r, c) in visited:
            continue
        visited.add((r, c))

        if (r, c) in intersections and (r, c) != pos:
            if not climbed:
                directional_graph[pos].append((d, (r, c)))
            graph[pos].append((d, (r, c)))
            continue

        for (nr, nc), n in neighbours(grid, r, c):
            if n in directional and (nr - r, nc - c) != directional[n]:
                queue.append((d + 1, (nr, nc), True))
            elif n != "#":
                queue.append((d + 1, (nr, nc), climbed))


def dfs(graph: dict, visited: set = set(), pos: tuple = start, dist: int = 0):
    if pos == end:
        return dist

    longest = 0
    visited.add(pos)
    for d, adj in graph[pos]:
        if adj in visited:
            continue
        longest = max(longest, dfs(graph, visited, adj, dist + d))
    visited.remove(pos)
    return longest


for intersection in intersections:
    intersection_search(intersection)

p1 = dfs(directional_graph)
print(p1)

p2 = dfs(graph)
print(p2)

if args.test:
    args.tester(p1, p2)
