#!/usr/bin/env python3.12

import aocutils as u
from sys import argv


def main(file: str) -> None:
    print('Day 9')

    moves = [(move[0], int(move[2:])) for move in u.input_as_lines(file)]

    D = {'R': (1, 0), 'L': (-1, 0), 'U': (0, -1), 'D': (0, 1)}
    hp = (0, 0)
    h = (0, 0)
    t = (0, 0)
    P = set()

    def addCoord(a: tuple, b: tuple) -> tuple:
        return (a[0] + b[0], a[1] + b[1])

    def dist(a: tuple, b: tuple) -> int:
        return max(abs(a[0] - b[0]), abs(a[1] - b[1]))

    P.add(t)
    for d, it in moves:
        for _ in range(it):
            hp = h
            h = addCoord(h, D[d])
            if (dist(h, t) > 1):
                t = hp
                P.add(t)
    p1 = len(P)
    print(f'{p1=}')

    # b is chasing after a
    # get bs new pos
    def chase(a: tuple, b: tuple) -> tuple:
        if dist(a, b) <= 1:
            return b
        ax, ay = a
        bx, by = b
        if ax == bx:
            return bx, (ay + by) // 2
        if ay == by:
            return (ax + bx) // 2, by
        for d in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
            m = addCoord(b, d)
            if dist(a, m) <= 1:
                return m

    R = [(0, 4)] * 10  # H 1 2 3 4 5 6 7 8 9
    P2 = set()
    P2.add(R[9])

    for d, it in moves:
        for _ in range(it):
            R[0] = addCoord(R[0], D[d])
            for i in range(1, len(R)):
                R[i] = chase(R[i-1], R[i])
            P2.add(R[9])
    p2 = len(P2)
    print(f'{p2=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '09.in'
    main(file)
