#!/usr/bin/env python3.12

import aocutils as u
from sys import argv


def part1(datastream: str) -> int:
    targetLen = 4
    for i in range(targetLen, len(datastream)):
        if len(set(datastream[i-targetLen:i])) == targetLen:
            return i


def part2(datastream: str) -> int:
    targetLen = 14
    for i in range(targetLen, len(datastream)):
        if len(set(datastream[i-targetLen:i])) == targetLen:
            return i


def main(file: str) -> None:
    print('Day 06')

    datastream = u.read_input(file)

    p1 = part1(datastream)
    print(f'{p1=}')

    p2 = part2(datastream)
    print(f'{p2=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '06.in'
    main(file)
