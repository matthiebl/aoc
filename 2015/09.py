"""
--- Day 9: All in a Single Night ---
https://adventofcode.com/2015/day/9
"""

from collections import defaultdict
from utils import *

args = parse_args(year=2015, day=9)
raw = get_input(args.filename, year=2015, day=9)

lines = raw.splitlines()
graph = defaultdict(list)
for line in lines:
    a, _, b, _, n = line.split()
    graph[a].append((int(n), b))
    graph[b].append((int(n), a))

p1 = float("inf")
p2 = 0
for n in graph:
    stack = [(0, n, set())]
    while stack:
        d, nxt, visited = stack.pop()
        if nxt in visited:
            continue
        visited.add(nxt)

        if len(visited) == len(graph):
            p1 = min(p1, d)
            p2 = max(p2, d)
            continue
        stack.extend([(d + w, pos, set(visited)) for w, pos in graph[nxt]])
print(p1)
print(p2)

if args.test:
    args.tester(p1, p2)
