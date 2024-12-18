"""
--- Day 18: RAM Run ---
https://adventofcode.com/2024/day/18
"""

from utils import *

args = parse_args(year=2024, day=18)
raw = get_input(args.filename, year=2024, day=18)

bytes = list(map(tuple, chunks(nums(raw))))

R, C = 70, 70


def to_graph(walls):
    graph: dict[tuple, list[tuple]] = {}
    for r in range(R + 1):
        for c in range(C + 1):
            if (r, c) in walls:
                continue
            graph[(r, c)] = []
            for dr, dc in directions():
                if 0 <= r + dr <= R and 0 <= c + dc <= C and (r + dr, c + dc) not in walls:
                    graph[(r, c)].append((1, (r + dr, c + dc)))
    return graph


walls = set(bytes[:1024])
graph = to_graph(walls)


def is_end(pos):
    return pos == (R, C)


p1 = dijkstras(graph, (0, 0), is_end)
print(p1)

l = 1024
h = len(bytes)

while l < h:
    m = (h + l) // 2
    graph = to_graph(set(bytes[:m]))
    r = dijkstras(graph, (0, 0), is_end)
    if isinstance(r, int):
        l = m + 1
    else:
        h = m
p2 = ",".join(map(str, bytes[l - 1]))
print(p2)

if args.test:
    args.tester(p1, p2)
