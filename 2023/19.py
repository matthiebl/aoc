#!/usr/bin/env python3.12

import aocutils as u
from sys import argv

Workflows = dict[str, tuple[list[tuple[str, str, int, str]], str]]

OPS = {
    '<': int.__lt__,
    '>': int.__gt__,
}
sections = {}


def intersection(xmas: u.Coords, kind):
    splits = [xmas]
    while splits:
        this = splits.pop()
        intersections = False
        for prev in sections:
            ranges = [u.range_overlap(r1, r2) for r1, r2 in zip(this, prev)]
            inter = [b for _, b, _ in ranges]
            if any(a is None for a in inter):
                # no intersection
                continue
            intersections = True
            # very ugly...
            for a in ranges[0]:
                if a is None:
                    continue
                for b in ranges[1]:
                    if b is None:
                        continue
                    for c in ranges[2]:
                        if c is None:
                            continue
                        for d in ranges[3]:
                            if d is None:
                                continue
                            if [a, b, c, d] == inter:
                                continue
                            splits.append([a, b, c, d])
            break
        if not intersections:
            sections[tuple(this)] = kind


def send(workflows: Workflows, name, xmas: dict[str, u.Coord]):
    if any(b - a <= 0 for a, b in xmas.values()):
        return
    if name == 'R' or name == 'A':
        intersection(xmas.values(), name)
        return
    rules, default = workflows[name]
    xxmas = xmas.copy()

    for (key, cmp, n, target) in rules:
        lo, hi = xxmas[key]
        xxxmas = xxmas.copy()
        if cmp == '>':
            xxxmas[key] = (max(lo, n + 1), hi)
            send(workflows, target, xxxmas)
            xxmas[key] = (lo, min(hi, n + 1))
        elif cmp == '<':
            xxxmas[key] = (lo, min(hi, n))
            send(workflows, target, xxxmas)
            xxmas[key] = (max(lo, n), hi)
    send(workflows, default, xxmas)


def is_accepted(workflows: Workflows, ratings: dict[str, int], name: str = 'in'):
    if name == 'A':
        return True
    if name == 'R':
        return False
    rules, default = workflows[name]
    for (key, cmp, n, target) in rules:
        if OPS[cmp](ratings[key], n):
            return is_accepted(workflows, ratings, target)
    return is_accepted(workflows, ratings, default)


def count(workflows: Workflows, ranges: dict[str, u.Coord], name: str = 'in'):
    if name == 'R':
        return 0
    if name == 'A':
        return u.mul(b - a for a, b in ranges.values())

    rules, default = workflows[name]
    total = 0
    for (key, cmp, n, target) in rules:
        lo, hi = ranges[key]
        T = n + 1, hi
        F = lo, n + 1
        if cmp == '<':
            T = lo, n
            F = n, hi
        if T[0] <= T[1]:
            copy = dict(ranges)
            copy[key] = T
            total += count(workflows, copy, target)
        if F[0] <= F[1]:
            ranges = dict(ranges)
            ranges[key] = F
        else:
            break
    else:
        total += count(workflows, ranges, default)

    return total


def main(file: str) -> None:
    print('Day 19')

    [instructions, parts] = u.input_from_grouped_lines(file)

    workflows: Workflows = {}
    for instruction in instructions:
        name, rules = instruction[:-1].split('{')
        rules = rules.split(',')
        workflows[name] = ([], rules.pop())
        for rule in rules:
            comparison, target = rule.split(':')
            key, cmp = comparison[0], comparison[1]
            n = int(comparison[2:])
            workflows[name][0].append((key, cmp, n, target))

    p1 = 0
    for rating in parts:
        item = {}
        for key, val in u.double_sep(rating[1:-1], ',', '='):
            item[key] = int(val)
        if is_accepted(workflows, item):
            p1 += sum(item.values())
    print(f'{p1=}')

    p2 = count(workflows,
               {'x': (1, 4001), 'm': (1, 4001), 'a': (1, 4001), 's': (1, 4001)})
    print(f'{p2=}')

    # This will find out where every single section of the ranges will end up
    # send(workflows, 'in',
    #      {'x': (1, 4001), 'm': (1, 4001), 'a': (1, 4001), 's': (1, 4001)})
    # p2 = 0
    # for r in sections:
    #     if sections[r] == 'A':
    #         p2 += u.mul(b - a for a, b in r)
    # print(f'{p2=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '19.in'
    main(file)
