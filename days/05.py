#!/usr/bin/env python3.10

from sys import argv
import re
import advent as adv


def merge_ranges(list_a, list_b):
    merged_ranges = []

    # Combine and sort the ranges from both lists
    all_ranges = sorted(list_a + list_b)
    print(all_ranges)

    # Iterate through the sorted ranges and merge or split as needed
    for i in range(len(all_ranges) - 1):
        lo1, hi1 = all_ranges[i]
        lo2, hi2 = all_ranges[i + 1]

        # If the current range overlaps with the next one, merge or split
        if lo1 <= lo2 < hi1:
            if lo1 != lo2 and (lo1, lo2) not in merged_ranges:
                merged_ranges.append((lo1, lo2))
            if lo2 != hi1 and (lo2, hi1) not in merged_ranges:
                merged_ranges.append((lo2, hi1))
            if hi1 != hi2 and (hi1, hi2) not in merged_ranges:
                merged_ranges.append((hi1, hi2))
        else:
            if (lo1, hi1) not in merged_ranges:
                merged_ranges.append((lo1, hi1))
            if (lo2, hi2) not in merged_ranges:
                merged_ranges.append((lo2, hi2))

    return merged_ranges


# Example usage:
list_a = [(0, 10), (10, 20)]
list_b = [(0, 5), (5, 10), (12, 25)]

result = merge_ranges(list_a, list_b)
print(result)


def map_mapping(input: tuple[int, int, int]) -> tuple[int, int, int]:
    dest, source, rang = input
    return source, source + rang, dest - source


def simplify(mappings: list[list[tuple[int, int, int]]]):
    while len(mappings) > 1:
        a = mappings.pop()
        b = mappings.pop()
        i, j, I, J = 0, 0, len(a), len(b)
        new = []


def convert(mapping: list[tuple[int, int, int]], input: int) -> int:
    for low, hi, change in mapping:
        if low <= input < hi:
            return input + change
    return input


def main(file: str) -> None:
    print('Day 05')

    data = adv.input_from_grouped_lines(file)

    seeds = list(map(int, re.findall('\d+', data[0][0])))

    mappings = [sorted([map_mapping(tuple(map(int, line.split(' '))))
                        for line in region[1:]], key=lambda t: t[0]) for region in data[1:]]

    p1 = 10 ** 20
    for seed in seeds:
        curr = seed
        for mapping in mappings:
            curr = convert(mapping, curr)
        p1 = min(p1, curr)
    print(p1)

    mappings.pop(0)
    mappings[0] = [(0, 15, 39), (15, 50, -15), (50, 54, -13),
                   (54, 98, 2), (98, 100, -49)]
    p1 = 10 ** 20
    for seed in seeds:
        curr = seed
        for mapping in mappings:
            curr = convert(mapping, curr)
        p1 = min(p1, curr)
    print(p1)


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '05.in'
    main(file)
