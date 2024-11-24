#!/usr/bin/env python3.12

from sys import argv

import aocutils as u


def two_sum(target: int, items: list[int]):
    store = set()
    for n in items:
        if target - n in store:
            return n * (target - n)
        store.add(n)
    return None


def main(file: str) -> None:
    print('Day 01')

    data = u.input_as_lines(file, map=int)
    target = 2020

    p1 = two_sum(2020, data)
    print(f'{p1=}')

    p2 = None
    for n in data:
        m = two_sum(target - n, data)
        if m:
            p2 = m * n
            break
    print(f'{p2=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '01.in'
    main(file)
