#!/usr/bin/env python3.12

import aocutils as u
from sys import argv, setrecursionlimit

setrecursionlimit(10000)


def main(file: str) -> None:
    print('Day 18')

    points = set(u.input_as_lines(
        file, map=lambda s: tuple(map(int, s.split(',')))))

    M = 1 + max(max(x for x, _, _ in points),
                max(y for _, y, _ in points),
                max(z for _, _, z in points))

    P = u.array_3D('.', M, M, M)

    p1 = 0
    DX = [-1, 1, 0, 0, 0, 0]
    DY = [0, 0, -1, 1, 0, 0]
    DZ = [0, 0, 0, 0, -1, 1]
    for x, y, z in points:
        P[z][y][x] = '#'
        SA = 6
        for dx, dy, dz in zip(DX, DY, DZ):
            if (x + dx, y + dy, z + dz) in points:
                SA -= 1
        p1 += SA
    print(f'{p1=}')

    air = set()

    def grow(x, y, z):
        air.add((x, y, z))
        for dx, dy, dz in zip(DX, DY, DZ):
            if ((x + dx, y + dy, z + dz) not in points
                    and (x + dx, y + dy, z + dz) not in air
                    and -1 <= x + dx <= M
                    and -1 <= y + dy <= M
                    and -1 <= z + dz <= M):
                grow(x + dx, y + dy, z + dz)

    grow(-1, -1, -1)

    p2 = 0
    for x, y, z in points:
        SA = 0
        for dx, dy, dz in zip(DX, DY, DZ):
            if (x + dx, y + dy, z + dz) in air:
                SA += 1
        p2 += SA
    print(f'{p2=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '18.in'
    main(file)
