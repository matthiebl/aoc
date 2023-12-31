#!/usr/bin/env python3.12

import aocutils as u
from sys import argv

"""
--- Day 19: Aplenty ---

This ended up being easier than I made it out to be.

For some reason, when solving the problem, I had assumed there would be overlapping
sections when I got an accepted part range in part 2 that I would have to remove.

I spent a long time making a function to union and manage the 4D ranges that I had
somehow produced through what I assume must have been a bug. Once I had finally got
this function working, I watched hyper-neutrino's video solution, which ended up
being a slightly modified version of my recursive function, that didn't bother with
any of the pointless range overlaps.

I then tried to refactor my function, and excluding the pointless overlap logic.
This ended up solving all of my issues and gave me the correct answer.

So went from having the correct answer in my grasp only a short time after the
puzzle's release, to pointlessly overcomplicating the problem.
"""

Workflows = dict[str, tuple[list[tuple[str, str, int, str]], str]]

OPS = {
    '<': int.__lt__,
    '>': int.__gt__,
}


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


def count_accepted(workflows: Workflows, ranges: dict[str, u.Coord], name: str = 'in'):
    if any(b - a <= 0 for a, b in ranges.values()):
        return 0
    if name == 'R':
        return 0
    if name == 'A':
        return u.mul(b - a for a, b in ranges.values())

    rules, default = workflows[name]
    total = 0
    for (key, cmp, n, target) in rules:
        lo, hi = ranges[key]
        if cmp == '>':
            copy = dict(ranges)
            copy[key] = (n + 1, hi)
            total += count_accepted(workflows, copy, target)
            ranges[key] = (lo, n + 1)
        elif cmp == '<':
            copy = dict(ranges)
            copy[key] = (lo, n)
            total += count_accepted(workflows, copy, target)
            ranges[key] = (n, hi)
    return total + count_accepted(workflows, ranges, default)


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

    p2 = count_accepted(workflows,
                        {'x': (1, 4001), 'm': (1, 4001), 'a': (1, 4001), 's': (1, 4001)})
    print(f'{p2=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '19.in'
    main(file)
