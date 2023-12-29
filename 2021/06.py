#!/usr/bin/env python3.12

import aocutils as u
from sys import argv


def main(file: str) -> None:
    print('Day 06')

    lanternfish = u.Counter(u.map_int(u.read_input(file).split(',')))

    def day():
        restarting = lanternfish.get(0, 0)
        lanternfish[0] = lanternfish[1]
        lanternfish[1] = lanternfish[2]
        lanternfish[2] = lanternfish[3]
        lanternfish[3] = lanternfish[4]
        lanternfish[4] = lanternfish[5]
        lanternfish[5] = lanternfish[6]
        lanternfish[6] = lanternfish[7] + restarting
        lanternfish[7] = lanternfish[8]
        lanternfish[8] = restarting

    for t in range(80):
        day()

    p1 = sum(lanternfish.values())
    print(f'{p1=}')

    for t in range(256 - 80):
        day()

    p2 = sum(lanternfish.values())
    print(f'{p2=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '06.in'
    main(file)
