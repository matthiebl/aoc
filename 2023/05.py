#!/usr/bin/env python3.12

import aocutils as u
from sys import argv

"""
--- Day 5: If You Give A Seed A Fertilizer ---

This was an hard challenge for so early...

Initial solution I implemented to solve the challenge was to work the
lowest location backwards to a seed. If that seed was in a range from
the seed ranges, then I found the correct seed, else move to a larger
location.

This worked fine, but far too slow...

Instead, lets just map across the ranges themselves. Instead of doing
one seed at a time, we can move the whole range of seeds across. If a
range overlaps a mapping range we can just do the non-intersecting
part as well. Eventaully we will convert a range, the whole way.

Do this for all ranges and we end up with all the outcome ranges from
the inputs. We then just need to lowest start of a range!
"""


def map_mapping(input: list[int, int, int]) -> tuple[int, int, int]:
    dest, source, rang = input
    return source, source + rang, dest - source


def convert(mapping: list[tuple[int, int, int]], input: int) -> int:
    for low, hi, change in mapping:
        if low <= input < hi:
            return input + change
    return input


def convert_range(ranges: list[tuple[int, int]], mapping: list[tuple[int, int, int]]) -> list[tuple[int, int]]:
    finished: list[tuple[int, int]] = []

    while ranges:
        lo, hi = ranges.pop()
        found = False
        for s, e, d in mapping:
            before, inter, after = u.range_overlap((lo, hi), (s, e))
            if inter is None:
                continue
            finished.append((inter[0] + d, inter[1] + d))
            if before:
                ranges.append(before)
            if after:
                ranges.append(after)
            found = True
            break
        if not found:
            # current range should just remain diff +0
            finished.append((lo, hi))

    return finished


def main(file: str) -> None:
    print('Day 05')

    data = u.input_from_grouped_lines(file)

    seeds = u.find_digits(data[0][0])
    mappings = [sorted([map_mapping(u.map_int(line.split(' ')))
                        for line in region[1:]], key=lambda t: t[0]) for region in data[1:]]

    p1 = 10 ** 20
    for seed in seeds:
        curr = seed
        for mapping in mappings:
            curr = convert(mapping, curr)
        p1 = min(p1, curr)
    print(f'{p1=}')

    seed_ranges = u.groups_of(seeds, 2)
    all_ranges = []
    for start, size in seed_ranges:
        ranges = [(start, start + size)]
        for mapping in mappings:
            # print(ranges)
            ranges = convert_range(ranges, mapping)
        all_ranges += ranges
    p2 = min(lo for lo, _ in all_ranges)
    print(f'{p2=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '05.in'
    main(file)
