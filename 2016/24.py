"""
--- Day 24: Air Duct Spelunking ---
https://adventofcode.com/2016/day/24
"""

from collections import defaultdict
from heapq import heappop, heappush
from utils import *

args = parse_args(year=2016, day=24)
raw = get_input(args.filename, year=2016, day=24)

grid = [list(line) for line in raw.splitlines()]
grid_graph = grid_to_graph(grid, valid_tiles=".0123456789")

start = next(find_in_grid(grid, "0"))
locations = list(find_in_grid(grid, "0123456789"))

graph = defaultdict(lambda: defaultdict(lambda: float("inf")))
for pos1 in locations:
    _, dists = dijkstras(grid_graph, pos1, is_end=lambda _: False)
    for pos2 in locations:
        graph[pos1][pos2] = dists[pos2]


def traverse(return_home: bool = False):
    pq = [(0, start, (start,))]
    while pq:
        d, p, vis = heappop(pq)
        if len(vis) == len(locations) + 1:
            return d
        if len(vis) == len(locations):
            if not return_home:
                return d
            dd = graph[p][start]
            heappush(pq, (d + dd, start, vis + (n,)))
        for n, dd in graph[p].items():
            if n not in vis:
                heappush(pq, (d + dd, n, vis + (n,)))


p1 = traverse()
print(p1)

p2 = traverse(return_home=True)
print(p2)

if args.test:
    args.tester(p1, p2)
