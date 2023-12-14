#!/usr/bin/env python3.12

import aocutils as u
from sys import argv


def main(file: str) -> None:
    print('Day 1')

    brackets = u.input_as_lines(file)[0]
    p1 = brackets.count('(') - brackets.count(')')
    print(f'{p1=}')

    p2 = 0
    level = 0
    for i, c in enumerate(brackets):
        if c == ')':
            level -= 1
        else:
            level += 1
        if level == -1:
            p2 = i + 1
            break
    print(f'{p2=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '01.in'
    main(file)
