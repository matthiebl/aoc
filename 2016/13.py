"""
--- Day 13: A Maze of Twisty Little Cubicles ---
https://adventofcode.com/2016/day/13
"""

from utils import *

args = parse_args(year=2016, day=13)
raw = get_input(args.filename, year=2016, day=13)

seed = next(nums(raw))


def is_free(r, c):
    v = c*c + 3*c + 2*c*r + r + r*r + seed
    return bin(v).count("1") % 2 == 0


def traverse(end):
    from heapq import heappop, heappush

    within_range = set()
    visited = set()
    pq = [(0, (1, 1))]
    while pq:
        d, nxt = heappop(pq)
        if nxt in visited:
            continue
        visited.add(nxt)
        if d <= 50:
            within_range.add(nxt)

        if nxt == end:
            return d, len(within_range)

        for dr, dc in directions():
            nr, nc = nxt[0] + dr, nxt[1] + dc
            if nr >= 0 and nc >= 0 and is_free(nr, nc):
                heappush(pq, (d + 1, (nr, nc)))


p1, p2 = traverse((39, 31))
print(p1)
print(p2)

if args.test:
    args.tester(p1, p2)
