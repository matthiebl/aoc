#!/usr/bin/env python3.12

import aocutils as u
from sys import argv

CYCLES = 10 ** 9


def rotate(lst):
    return [list(c) for c in zip(*lst[::-1])]


def roll(table: list[list[str]]):
    for row in table:
        i = len(row) - 2
        j = i
        while i >= 0:
            if row[i] == 'O':
                while j < len(row) - 1 and row[j + 1] == '.':
                    j += 1
                row[i] = '.'
                row[j] = 'O'
            i -= 1
            j = i


def cycle(table):
    for _ in range(4):
        table = rotate(table)
        roll(table)
    return table


def main(file: str) -> None:
    print('Day 14')

    data = u.input_as_lines(file)

    platform = rotate(data)

    roll(platform)
    p1 = 0
    for row in platform:
        for i, c in enumerate(row):
            if c == 'O':
                p1 += i + 1
    print(f'{p1=}')

    prev_state = {}
    platform = data
    i = 0
    while i < CYCLES:
        platform = cycle(platform)

        platform_hash = tuple(str(r) for r in platform)
        if platform_hash in prev_state:
            skippable = i - prev_state[platform_hash]
            remaining_cycles = CYCLES - i
            i += skippable * (remaining_cycles // skippable)
        prev_state[platform_hash] = i
        i += 1

    platform = rotate(platform)
    p2 = 0
    for row in platform:
        for i, c in enumerate(row):
            if c == 'O':
                p2 += i + 1
    print(f'{p2=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '14.in'
    main(file)
