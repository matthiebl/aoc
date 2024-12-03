#!/usr/bin/env python3.12

import re
from sys import argv

import aocutils as u


def main(file: str) -> None:
    print('Day 03')

    data = u.input_as_lines(file)

    p1 = 0
    p2 = 0
    enabled = True
    for line in data:
        parts = re.findall(r'mul\(\d{1,3},\d{1,3}\)', line)
        for part in parts:
            i = part.index(',')
            p1 += int(part[4:i]) * int(part[i+1:-1])

        parts_2 = re.findall(r'mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)', line)
        for part in parts_2:
            if part == 'do()':
                enabled = True
            elif part == 'don\'t()':
                enabled = False
            elif enabled:
                i = part.index(',')
                p2 += int(part[4:i]) * int(part[i+1:-1])

    print(f'{p1=}')
    print(f'{p2=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '03.in'
    main(file)
