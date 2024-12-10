#!/usr/bin/env python3.13

from collections import Counter, defaultdict
from sys import argv

from maoc import fetch, submit
# from maoc.utils.classes import Point
from maoc.utils.collect import chunks, windows

# from maoc.utils.parse import ints

"""
--- Day 9: ---

https://adventofcode.com/2024/day/9
"""

print("Day 09")
FILE_NAME = argv[1] if len(argv) >= 2 else "09.in"
data = fetch(year=2024, day=9, path=__file__, file_name=FILE_NAME)


def checksum(system):
    cs = 0
    for i, id_ in enumerate(system):
        if id_ == ".":
            continue
        cs += i * int(id_)
    return cs


def part_one():
    system = []
    id_ = 0
    for i in range(0, len(data), 2):
        system += [id_] * int(data[i])
        if i + 1 < len(data):
            system += ["."] * int(data[i+1])
        id_ += 1
    l = system.index(".")
    r = len(system) - 1
    while l < r:
        system[l] = system[r]
        system[r] = "."
        l += 1
        r -= 1
        while system[l] != "." and l < r:
            l += 1
        while system[r] == "." and l < r:
            r -= 1
    return checksum(system)


def part_two():
    system = []
    id_ = 0
    for i in range(0, len(data), 2):
        system.append((id_, int(data[i])))
        if i + 1 < len(data):
            system.append((".", int(data[i+1])))
        id_ += 1

    def to_flat(system):
        flat = []
        for i, s in system:
            flat += [i] * s
        return flat

    known_f = len(system) - 1
    id_ -= 1
    while id_ > 0:
        f = known_f
        while f > 0:
            search, size = system[f]
            if search == id_:
                break
            f -= 1
        known_f = f
        for i, (b, free) in enumerate(system):
            if b != ".":
                continue
            if free < size:
                continue
            if i > f:
                break

            system[i] = (id_, size)
            system[f] = (".", size)
            if free > size:
                if system[i + 1][0] == ".":
                    system[i + 1] = (".", free - size + system[i + 1][1])
                else:
                    system.insert(i + 1, (".", free - size))
            break
        id_ -= 1
    flat = to_flat(system)
    return checksum(flat)


submit(year=2024, day=9, part=1, solution=part_one, verbose=True)
submit(year=2024, day=9, part=2, solution=part_two, verbose=True)
