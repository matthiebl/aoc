#!/usr/bin/env python3.12

import aocutils as u
from sys import argv


def main(file: str) -> None:
    print('Day 2')

    dimensions = u.input_as_lines(file, map=lambda l: u.map_int(l.split('x')))

    p1 = 0
    p2 = 0
    for [a, b, c] in dimensions:
        area = [a * b, b * c, a * c]
        p1 += min(area) + 2 * sum(area)
        perim = [2 * (a + b), 2 * (b + c), 2 * (a + c)]
        p2 += min(perim) + a * b * c
    print(f'{p1=}')
    print(f'{p2=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '02.in'
    main(file)
