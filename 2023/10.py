"""
--- Day 10: Pipe Maze ---
https://adventofcode.com/2023/day/10
"""

from collections import deque
from re import findall
from utils import *

args = parse_args(year=2023, day=10)
raw = get_input(args.filename, year=2023, day=10)

grid = [list(line) for line in raw.splitlines()]
R, C = len(grid), len(grid[0])

sr, sc = next(find_in_grid(grid, "S"))

s_check = {
    (-1, 0): "|7F",
    (0,  1): "-J7",
    (1,  0): "|LJ",
    (0, -1): "-LF",
}
s_pipe = {
    (-1, 0, 0, 1):  "L",
    (0, 1, 1, 0):   "F",
    (1, 0, 0, -1):  "7",
    (-1, 0, 0, -1): "J",
    (-1, 0, 1, 0):  "|",
    (0, 1, 0, -1):  "-",
}

graph: dict[tuple, list] = {}
for (r, c), v, _ in enumerate_grid(grid):
    if v == "|":
        graph[(r, c)] = [(1, (r - 1, c)), (1, (r + 1, c))]
    elif v == "-":
        graph[(r, c)] = [(1, (r, c - 1)), (1, (r, c + 1))]
    elif v == "L":
        graph[(r, c)] = [(1, (r - 1, c)), (1, (r, c + 1))]
    elif v == "J":
        graph[(r, c)] = [(1, (r - 1, c)), (1, (r, c - 1))]
    elif v == "7":
        graph[(r, c)] = [(1, (r + 1, c)), (1, (r, c - 1))]
    elif v == "F":
        graph[(r, c)] = [(1, (r + 1, c)), (1, (r, c + 1))]
    elif v == "S":
        t = ()
        graph[(r, c)] = []
        for (dr, dc), check in s_check.items():
            if within_grid(grid, r + dr, c + dc) and grid[r + dr][c + dc] in check:
                graph[(r, c)].append((1, (r + dr, c + dc)))
                t = t + (dr, dc)
        grid[r][c] = s_pipe[t]

_, dists = dijkstras(graph, (sr, sc), is_end_pos(-1, -1))
p1 = max(d for d in dists.values() if d != float("inf"))
print(p1)

pipe = set(p for p, d in dists.items() if d != float("inf"))
assert (0, 0) not in pipe


def flood_fill(start: tuple):
    seen = set()
    queue = deque([start])
    while queue:
        r, c = queue.popleft()
        if not within_grid(grid, r, c) or (r, c) in seen or (r, c) in pipe:
            continue
        seen.add((r, c))
        for dr, dc in directions():
            queue.append((r + dr, c + dc))
    return seen


p2 = 0
grid = [[v if (r, c) in pipe else "." for c, v in enumerate(row)] for r, row in enumerate(grid)]
for (r, c), v, _ in enumerate_grid(grid):
    if (r, c) in pipe:
        continue
    straights = grid[r][c:].count("|")
    corners = len(findall(r"L|7", "".join(grid[r][c:]))) // 2 - len(findall(r"F|J", "".join(grid[r][c:]))) // 2
    p2 += 1 if (straights + corners) % 2 == 1 else 0

print(p2)

if args.test:
    args.tester(p1, p2)
