"""
--- Day 18: RAM Run ---
https://adventofcode.com/2024/day/18
"""

from utils import *

N = 70
L = 1024

args = parse_args(year=2024, day=18)
raw = get_input(args.filename, year=2024, day=18)

bytes = list(map(tuple, chunks(nums(raw))))
graph = grid_to_graph(create_grid(N + 1, N + 1, blocks=[(r, c, "#") for r, c in bytes[:L]]), valid_tiles=".")

p1, _ = bfs(graph, (0, 0), is_end_pos(N, N))
print(p1)

l, h = L, len(bytes)
while l < h:
    m = (h + l) // 2
    graph = grid_to_graph(create_grid(N + 1, N + 1, blocks=[(r, c, "#") for r, c in bytes[:m]]), valid_tiles=".")
    if bfs(graph, (0, 0), is_end_pos(N, N))[0] is not None:
        l = m + 1
    else:
        h = m
p2 = ",".join(map(str, bytes[l - 1]))
print(p2)

if args.test:
    args.tester(p1, p2)
