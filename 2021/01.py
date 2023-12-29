#!/usr/bin/env python3.12

import aocutils as u
from sys import argv


def main(file: str) -> None:
    print('Day 01')

    depths = u.input_as_lines(file, map=int)

    p1 = sum(1 if d2 > d1 else 0 for d1, d2 in zip(depths, depths[1:]))
    print(f'{p1=}')

    window_sums = [sum((a, b, c)) for a, b, c in zip(depths, depths[1:], depths[2:])]
    p2 = sum(1 if d2 > d1 else 0 for d1, d2 in zip(window_sums, window_sums[1:]))
    print(f'{p2=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '01.in'
    main(file)
