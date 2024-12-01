#!/usr/bin/env python3.12

from sys import argv

import aocutils as u


def main(file: str) -> None:
    print('Day 01')

    pairs = u.input_as_lines(file, map=lambda p: u.map_int(p.split()))
    left = sorted(x for x, _ in pairs)
    right = sorted(y for _, y in pairs)

    p1 = sum(abs(x - y) for x, y in zip(left, right))
    print(f'{p1=}')

    p2 = sum(x * right.count(x) for x in left)
    print(f'{p2=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '01.in'
    main(file)
