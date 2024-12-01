#!/usr/bin/env python3.12

from sys import argv

import aocutils as u


def iter(code: str) -> str:
    new = ''
    c = code[0]
    l = 0
    for i in range(len(code)):
        if code[i] == c:
            l += 1
        else:
            new += f'{l}{c}'
            c = code[i]
            l = 1
    new += f'{l}{c}'
    return new


def main(file: str) -> None:
    print('Day 10')

    code = u.read_input(file)

    iterated = code
    for _ in range(40):
        iterated = iter(iterated)
    p1 = len(iterated)
    print(f'{p1=}')

    for _ in range(10):
        iterated = iter(iterated)
    p2 = len(iterated)
    print(f'{p2=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '10.in'
    main(file)
