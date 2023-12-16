#!/usr/bin/env python3.12

import aocutils as u
from sys import argv, setrecursionlimit

setrecursionlimit(1000000)


def main(file: str) -> None:
    print('Day 16')

    data = u.input_as_lines(file)

    V = set()
    P = set()

    def travel(x, y, dx, dy):
        if (x, y, dx, dy) in P:
            return
        P.add((x, y, dx, dy))
        V.add((x, y))

        if not u.in_grid(data, y + dy, x + dx):
            return

        nx, ny = x + dx, y + dy
        c = data[ny][nx]

        if c == '.' or (dx != 0 and c == '-') or (dy != 0 and c == '|'):
            travel(nx, ny, dx, dy)
        elif c == '/' and dx != 0:
            travel(nx, ny, 0, -dx)
        elif c == '/' and dy != 0:
            travel(nx, ny, -dy, 0)
        elif c == '\\' and dx != 0:
            travel(nx, ny, 0, dx)
        elif c == '\\' and dy != 0:
            travel(nx, ny, dy, 0)
        elif c == '|':
            travel(nx, ny, 0, -1)
            travel(nx, ny, 0, 1)
        elif c == '-':
            travel(nx, ny, -1, 0)
            travel(nx, ny, 1, 0)
        else:
            assert False

    travel(-1, 0, 1, 0)
    p1 = len(V) - 1
    print(f'{p1=}')

    H = len(data)
    W = len(data[0])

    best = p1
    for i in range(H):
        V.clear()
        P.clear()
        travel(-1, i, 1, 0)
        energised = len(V) - 1
        best = max(best, energised)

        V.clear()
        P.clear()
        travel(W, i, -1, 0)
        energised = len(V) - 1
        best = max(best, energised)

    for i in range(W):
        V.clear()
        P.clear()
        travel(i, -1, 0, 1)
        energised = len(V) - 1
        best = max(best, energised)

        V.clear()
        P.clear()
        travel(i, H, 0, -1)
        energised = len(V) - 1
        best = max(best, energised)

    p2 = best
    print(f'{p2=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '16.in'
    main(file)
