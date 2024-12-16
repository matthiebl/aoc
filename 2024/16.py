"""
--- Day 16: Warehouse Woes ---
https://adventofcode.com/2024/day/16
"""

from heapq import heapify, heappush, heappop
from utils import *

args = parse_args(year=2024, day=16)
raw = get_input(args["filename"], year=2024, day=16)

grid = [list(line) for line in raw.splitlines()]
R, C = len(grid), len(grid[0])

sr, sc = (R - 2, 1)
er, ec = (1, C - 2)
grid[sr][sc] = "."
grid[er][ec] = "."

g = {}

D = {
    "N": list(zip("WNE", directions([3, 1, 5]))),
    "E": list(zip("NES", directions([1, 5, 7]))),
    "S": list(zip("ESW", directions([5, 7, 3]))),
    "W": list(zip("SWN", directions([7, 3, 1]))),
}

for (r, c), val, _ in enumerate_grid(grid):
    if val == "#":
        continue
    for d in "NESW":
        g[(r, c, d)] = []
        for i, (dd, (dr, dc)) in enumerate(D[d]):
            if grid[r + dr][c + dc] == ".":
                cost = 1001 if i % 3 != 1 else 1
                g[(r, c, d)].append((cost, (r + dr, c + dc, dd)))


def dijkstras(graph: dict, start, initial_dist: int = 0):
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


dists = dijkstras(g, (sr, sc, "E"))

shortest_path = min([dists[(r, c, d)] for r, c, d in dists if r == er and c == ec], key=lambda t: t["w"])
p1 = shortest_path["w"]
print(p1)

vis = set()


def positions(paths: list) -> int:
    if len(paths) == 0:
        return
    vis.update([(r, c) for r, c, _ in paths])
    [positions(dists[pos]["paths"]) for pos in paths]


positions(shortest_path["paths"])
p2 = len(vis) + 1
print(p2)

assert p1 == 66404
assert p2 == 433
