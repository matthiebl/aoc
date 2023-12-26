#!/usr/bin/env python3.12

import aocutils as u
from sys import argv


def main(file: str) -> None:
    print('Day 04')

    pairs = u.input_as_lines(file, map=lambda s: u.double_sep(
        s, ',', '-', map=int, group=tuple))

    p1 = sum((x1 <= y1 and y2 <= x2) or (y1 <= x1 and x2 <= y2)
             for (x1, x2), (y1, y2) in pairs)
    print(f'{p1=}')

    p2 = sum((x1 <= y1 <= x2) or (y1 <= x1 <= y2)
             for (x1, x2), (y1, y2) in pairs)
    print(f'{p2=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '04.in'
    main(file)
