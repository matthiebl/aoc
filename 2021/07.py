#!/usr/bin/env python3.12

import aocutils as u
from sys import argv


def main(file: str) -> None:
    print('Day 07')

    crabs = u.map_int(u.read_input(file).split(','))

    p1 = 10 ** 10
    p2 = 10 ** 10
    for x in range(min(crabs), max(crabs) + 1):
        a, b = 0, 0
        for crab in crabs:
            n = abs(x - crab)
            a += n
            b += (n * (n + 1)) // 2
        p1 = min(p1, a)
        p2 = min(p2, b)
    print(f'{p1=}')
    print(f'{p2=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '07.in'
    main(file)
