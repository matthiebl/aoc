"""
--- Day 14: Disk Defragmentation ---
https://adventofcode.com/2017/day/14
"""

from collections import deque

from utils import *

knot_hash = import_day("2017.10", "knot_hash")

args = parse_args(year=2017, day=14)
raw = get_input(args.filename, year=2017, day=14)

grid = [bin(int(knot_hash(f"{raw}-{i}"), 16))[2:].rjust(128, "0") for i in range(128)]
used = set(find_in_grid(grid, "1"))

p1 = len(used)
print(p1)


def region(start: str = "0"):
    queue = deque([start])
    region = set()
    while queue:
        (r, c) = queue.popleft()
        if (r, c) in region:
            continue
        region.add((r, c))
        for pos, v in neighbours(grid, r, c):
            if v == "1":
                queue.append(pos)
    return region


p2 = 0
while used:
    used -= region(used.pop())
    p2 += 1
print(p2)

if args.test:
    args.tester(p1, p2)
