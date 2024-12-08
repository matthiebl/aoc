#!/usr/bin/env python3.13

from collections import Counter, defaultdict
from sys import argv

from maoc import fetch, submit

# from maoc.utils.classes import Point
# from maoc.utils.collect import chunks, windows
# from maoc.utils.parse import ints

"""
--- Day 8: ---

https://adventofcode.com/2024/day/8
"""

print("Day 08")
FILE_NAME = argv[1] if len(argv) >= 2 else "08.in"
raw = fetch(year=2024, day=8, path=__file__, file_name=FILE_NAME).splitlines()

R = len(raw)
C = len(raw[0])


def parse_raw():
    d = defaultdict(set)
    for r, line in enumerate(raw):
        for c, ch in enumerate(line):
            if ch != ".":
                d[ch].add((r, c))
    return {k: list(v) for k, v in d.items()}


data = parse_raw()


def part_one():
    antinodes = set()
    for freq in data:
        for i, (r1, c1) in enumerate(data[freq]):
            for (r2, c2) in data[freq][i+1:]:
                dr, dc = r2 - r1, c2 - c1
                antinodes.add((r1 - dr, c1 - dc))
                antinodes.add((r2 + dr, c2 + dc))
    return sum(1 for r, c in antinodes if 0 <= r < R and 0 <= c < C)


def part_two():
    antinodes = set()
    for freq in data:
        for i, (r1, c1) in enumerate(data[freq]):
            for (r2, c2) in data[freq][i+1:]:
                dr, dc = r2 - r1, c2 - c1
                ir, ic = r1, c1
                while 0 <= ir < R and 0 <= ic < C:
                    antinodes.add((ir, ic))
                    ir += dr
                    ic += dc
                ir, ic = r1, c1
                while 0 <= ir < R and 0 <= ic < C:
                    antinodes.add((ir, ic))
                    ir -= dr
                    ic -= dc
    return len(antinodes)


submit(year=2024, day=8, part=1, solution=part_one)
submit(year=2024, day=8, part=2, solution=part_two)
