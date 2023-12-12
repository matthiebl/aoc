#!/usr/bin/env python3.12

from sys import argv
import re
import aocutils as u


def map_mapping(input: tuple[int, int, int]) -> tuple[int, int, int]:
    dest, source, rang = input
    return source, source + rang, dest - source


def missing_region(l: list[tuple[int, int, int]]) -> bool:
    _, lend, _ = l[0]
    for start, end, _ in l[1:]:
        if lend != start:
            return True
        lend = end
    return False


def clean_up_list(l: list[tuple[int, int, int]]):
    if l[0][0] != 0:
        l.insert(0, (0, l[0][0], 0))

    while missing_region(l):
        _, lend, _ = l[0]
        for i, (start, end, _) in enumerate(l[1:]):
            if lend != start:
                l.insert(i + 1, (lend, start, 0))
                break
            lend = end
    return l


def converge(l1: list[tuple[int, int, int]], l2: list[tuple[int, int, int]]):
    l1_max, l2_max = l1[-1][1], l2[-1][1]
    if l1_max > l2_max:
        l2.append((l2_max, l1_max, 0))
    elif l2_max > l1_max:
        l1.append((l1_max, l2_max, 0))

    new = []
    while l1 and l2:
        a1, a2, a3 = l1.pop(0)
        b1, b2, b3 = l2.pop(0)
        if a2 < b2:
            new.append((a1, a2, a3 + b3))
            l2.insert(0, (a2, b2, b3))
        elif b2 < a2:
            new.append((b1, b2, a3 + b3))
            l1.insert(0, (b2, a2, a3))
        else:
            new.append((a1, a2, a3 + b3))

    new_new = []
    a1, a2, a3 = new.pop(0)
    while new:
        b1, b2, b3 = new.pop(0)
        if a2 == b1 and a3 == b3:
            a2 = b2
        else:
            new_new.append((a1, a2, a3))
            a1, a2, a3 = b1, b2, b3
    new_new.append((a1, a2, a3))

    return new_new


def simplify(mappings: list[list[tuple[int, int, int]]]):
    while len(mappings) > 1:
        a = mappings.pop(0)
        b = mappings.pop(0)
        converged = converge(clean_up_list(a), clean_up_list(b))
        mappings.insert(0, converged)


def convert(mapping: list[tuple[int, int, int]], input: int) -> int:
    for low, hi, change in mapping:
        if low <= input < hi:
            return input + change
    return input


def reverse_mappings(mappings: list[list[tuple[int, int, int]]]):
    mappings.reverse()
    for i, mapping in enumerate(mappings):
        mappings[i] = [(l + inc, h + inc, -inc) for l, h, inc in mapping]


def in_range(seed: int, ranges: list[int]):
    for i in range(0, len(ranges), 2):
        if ranges[i] <= seed < ranges[i] + ranges[i + 1]:
            return True
    return False


def main(file: str) -> None:
    print('Day 05')

    data = u.input_from_grouped_lines(file)

    seeds = list(map(int, re.findall('\d+', data[0][0])))

    mappings = [sorted([map_mapping(tuple(map(int, line.split(' '))))
                        for line in region[1:]], key=lambda t: t[0]) for region in data[1:]]

    p1 = 10 ** 20
    for seed in seeds:
        curr = seed
        for mapping in mappings:
            curr = convert(mapping, curr)
        p1 = min(p1, curr)
    print(f'{p1=}')

    reverse_mappings(mappings)

    p2 = 0
    while True:
        curr = p2
        for mapping in mappings:
            curr = convert(mapping, curr)
        if in_range(curr, seeds):
            break
        p2 += 1
    print(f'{p2=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '05.in'
    main(file)
