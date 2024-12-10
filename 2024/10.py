#!/usr/bin/env python3.13

from collections import Counter, defaultdict
from sys import argv
from maoc import fetch, submit
from maoc.utils.classes import Point
from maoc.utils.collect import chunks, windows
from maoc.utils.parse import ints

"""
--- Day 10: ---

https://adventofcode.com/2024/day/10
"""

print("Day 10")
FILE_NAME = argv[1] if len(argv) >= 2 else "10.in"
raw = fetch(year=2024, day=10, path=__file__, file_name=FILE_NAME)


def parse_raw():
    return [list(line) for line in raw.splitlines()]


grid = parse_raw()

R = len(grid)
C = len(grid[0])


def trail_heads() -> list[tuple]:
    return [(r, c) for r, row in enumerate(grid) for c, ch in enumerate(row) if ch == "0"]


trail_ends = defaultdict(set)


def trail_head_score(start, pos) -> int:
    r, c = pos
    ch = int(grid[r][c])
    if ch == 9:
        trail_ends[start].add(pos)
        return 1
    score = 0
    for p in Point.neighbours_of(index_order=Point.NEIGHBOURS_4):
        dr, dc = p.to_rc()
        nr, nc = r + dr, c + dc
        if 0 <= nr < R and 0 <= nc < C and int(grid[nr][nc]) == ch + 1:
            score += trail_head_score(start, (nr, nc))
    return score


p2 = 0
for pos in trail_heads():
    p2 += trail_head_score(pos, pos)
p1 = sum(len(s) for s in trail_ends.values())

submit(year=2024, day=10, part=1, solution=p1, verbose=True)
submit(year=2024, day=10, part=2, solution=p2, verbose=True)
