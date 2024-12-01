#!/usr/bin/env python3.12

from sys import argv

import aocutils as u


def main(file: str) -> None:
    print('Day 01')

    data = u.input_as_lines(file)
    a = []
    b = []
    for l in data:
        l = l.split()
        x = int(l[0])
        y = int(l[1])
        a.append(x)
        b.append(y)
    a = sorted(a)
    b = sorted(b)

    p1 = 0
    for x, y in zip(a, b):
        p1 += abs(x - y)
    print(p1)

    p2 = 0
    for x in a:
        c = b.count(x)
        p2 += x * c
    print(p2)


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '01.in'
    main(file)
