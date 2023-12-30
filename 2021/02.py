#!/usr/bin/env python3.12

import aocutils as u
from sys import argv


def main(file: str) -> None:
    print('Day 02')

    instructions = [(i, int(n)) for i, n in u.input_as_lines(file, map=lambda l: l.split())]

    x, d = (0, 0)
    x2, d2, aim = (0, 0, 0)

    for ins, n in instructions:
        if ins == 'forward':
            x += n
            x2 += n
            d2 += aim * n
        elif ins == 'down':
            d += n
            aim += n
        else:
            d -= n
            aim -= n

    p1 = x * d
    print(f'{p1=}')
    p2 = x2 * d2
    print(f'{p2=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '02.in'
    main(file)
