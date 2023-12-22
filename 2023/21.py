#!/usr/bin/env python3.12

import aocutils as u
from sys import argv, setrecursionlimit

setrecursionlimit(26501365 + 100)

DX = [0, 1, 0, -1]
DY = [-1, 0, 1, 0]


def find(field, f):
    for y, row in enumerate(field):
        for x, c in enumerate(row):
            if c == f:
                return (x, y)


def main(file: str) -> None:
    print('Day 21')

    field = u.input_as_lines(file)

    POS = set([find(field, 'S')])

    def step(POS: set, steps):
        u.array_visualise(u.array_collect_def(POS))
        if steps == 0:
            return
        new = set()
        for x, y in POS:
            for d in range(4):
                nx, ny = x + DX[d], y + DY[d]
                if u.in_grid(field, ny, nx) and field[ny][nx] in '.S':
                    new.add((nx, ny))
        POS.clear()
        for n in new:
            POS.add(n)
        step(POS, steps - 1)

    step(POS, 64)
    p1 = len(POS)
    print(f'{p1=}')

    step(POS, 1)
    p1 = len(POS)
    print(f'{p1=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '21.in'
    main(file)
