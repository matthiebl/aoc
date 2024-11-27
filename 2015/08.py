#!/usr/bin/env python3.12

from sys import argv

import aocutils as u


def main(file: str) -> None:
    print('Day 08')

    data = u.input_as_lines(file)
    code = sum(len(x) for x in data)

    extras = 0

    chars = 0
    for string in data:
        curr = string[1:-1]
        extras += 4
        i = 0
        while i < len(curr):
            chars += 1
            if curr[i] != '\\':
                i += 1
                continue
            n = curr[i+1:i+2]
            extras += 1
            if n == '\\' or n == '"':
                i += 2
                extras += 1
            elif n == 'x':
                i += 4
            else:
                raise ValueError(f'String: "{curr}", current: {curr[i]}:{n}')
    p1 = code - chars
    print(f'{p1=}')

    p2 = extras
    print(f'{p2=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '08.in'
    main(file)
