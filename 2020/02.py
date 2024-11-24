#!/usr/bin/env python3.12

from sys import argv

import aocutils as u


def main(file: str) -> None:
    print('Day 02')

    data = u.input_as_lines(file, map=str.split)

    p1 = sum(int(r.split('-')[0]) <= pw.count(c[0]) <= int(r.split('-')[1]) for [r, c, pw] in data)
    print(f'{p1=}')

    p2 = sum((pw[int(r.split('-')[0]) - 1] + pw[int(r.split('-')[1]) - 1]).count(c[0]) == 1 for [r, c, pw] in data)
    print(f'{p2=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '02.in'
    main(file)
