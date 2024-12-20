"""
--- Day 16: Reindeer Maze ---
https://adventofcode.com/2024/day/16

Today I have solved the problem with Dijkstra's algorithm, where I not only
keep a graph of a position to adjacent, but a graph of position and direction
to possible moves, with the weighting including the cost to turn 90 deg.
"""

from heapq import heapify, heappush, heappop
from collections import deque
from utils import *

args = parse_args(year=2024, day=16)
raw = get_input(args.filename, year=2024, day=16)

grid = [list(line) for line in raw.splitlines()]
R, C = len(grid), len(grid[0])

sr, sc = (R - 2, 1)
er, ec = (1, C - 2)

D = {
    "N": list(zip("WNE", directions([3, 1, 5]))),
    "E": list(zip("NES", directions([1, 5, 7]))),
    "S": list(zip("ESW", directions([5, 7, 3]))),
    "W": list(zip("SWN", directions([7, 3, 1]))),
}

graph = {}
for (r, c), val, _ in enumerate_grid(grid, skip="#"):
    for d in "NESW":
        graph[(r, c, d)] = []
        for i, (dd, (dr, dc)) in enumerate(D[d]):
            if grid[r + dr][c + dc] in ".SE":
                cost = 1001 if i % 3 != 1 else 1
                graph[(r, c, d)].append((cost, (r + dr, c + dc, dd)))


def dijkstras(graph: dict, start, initial_dist: int = 0):
    """
    Modified Dijkstra's algorithm to keep track of the weight and
    positions that made us arrive at the shortest path so we can
    reconstruct the shortest paths.
    """
    distances = {pos: {"w": float("inf"), "paths": []} for pos in graph}
    distances[start]["w"] = initial_dist

    visited = set()

    heap = [(initial_dist, start)]
    heapify(heap)

    while heap:
        d, nxt = heappop(heap)
        if nxt in visited:
            continue
        visited.add(nxt)

        if nxt[0] == er and nxt[1] == ec:
            return distances

        for w, adj in graph[nxt]:
            tentative = d + w
            if tentative == distances[adj]["w"]:
                distances[adj]["paths"].append(nxt)
            elif tentative < distances[adj]["w"]:
                distances[adj] = {"w": tentative, "paths": [nxt]}
            heappush(heap, (tentative, adj))

    return distances


dists = dijkstras(graph, (sr, sc, "E"))

shortest_path = min([dists[(r, c, d)] for r, c, d in dists if r == er and c == ec], key=lambda t: t["w"])
p1 = shortest_path["w"]
print(p1)

visited = set()
queue = deque(shortest_path["paths"])
while queue:
    r, c, d = queue.popleft()
    visited.add((r, c))
    queue.extend(dists[(r, c, d)]["paths"])
p2 = len(visited) + 1
print(p2)

if args.test:
    args.tester(p1, p2)
