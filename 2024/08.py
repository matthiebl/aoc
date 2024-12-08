#!/usr/bin/env python3.13

from collections import defaultdict
from sys import argv

from maoc import fetch, submit

"""
--- Day 8: Resonant Collinearity ---

https://adventofcode.com/2024/day/8
"""

print("Day 08")
FILE_NAME = argv[1] if len(argv) >= 2 else "08.in"
raw = fetch(year=2024, day=8, path=__file__, file_name=FILE_NAME).splitlines()

R = len(raw)
C = len(raw[0])


def parse_raw():
    antennas = defaultdict(list)
    for r, line in enumerate(raw):
        for c, ch in enumerate(line):
            if ch != ".":
                antennas[ch].append((r, c))
    return antennas


antennas = parse_raw()


def part_one():
    nodes = set()
    for freq in antennas:
        for i, (r1, c1) in enumerate(antennas[freq]):
            for (r2, c2) in antennas[freq][i+1:]:
                dr, dc = r2 - r1, c2 - c1
                nodes.add((r1 - dr, c1 - dc))
                nodes.add((r2 + dr, c2 + dc))
    return sum(1 for r, c in nodes if 0 <= r < R and 0 <= c < C)


def part_two():
    nodes = set()
    for freq in antennas:
        for i, (r1, c1) in enumerate(antennas[freq]):
            for (r2, c2) in antennas[freq][i+1:]:
                dr, dc = r2 - r1, c2 - c1
                ir, ic = r1, c1
                while 0 <= ir < R and 0 <= ic < C:
                    nodes.add((ir, ic))
                    ir, ic = ir + dr, ic + dc
                ir, ic = r1, c1
                while 0 <= ir < R and 0 <= ic < C:
                    nodes.add((ir, ic))
                    ir, ic = ir - dr, ic - dc
    return len(nodes)


submit(year=2024, day=8, part=1, solution=part_one)
submit(year=2024, day=8, part=2, solution=part_two)
