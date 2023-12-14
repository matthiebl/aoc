#!/usr/bin/env python3.12

import aocutils as u
from sys import argv

DIR = {
    '>': (1, 0),
    '<': (-1, 0),
    '^': (0, -1),
    'v': (0, 1),
}


def main(file: str) -> None:
    print('Day 3')

    directions = u.read_input(file)

    V = set()
    pos = (0, 0)
    V.add(pos)
    for d in directions:
        pos = u.add_tup(pos, DIR[d])
        V.add(pos)
    p1 = len(V)
    print(f'{p1=}')

    V = set()
    robot = (0, 0)
    santa = (0, 0)
    V.add(santa)
    pairs = u.groups_of(directions, 2)
    for pair in pairs:
        santa = u.add_tup(santa, DIR[pair[0]])
        robot = u.add_tup(robot, DIR[pair[1]])
        V.add(santa)
        V.add(robot)
    p2 = len(V)
    print(f'{p2=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '03.in'
    main(file)
