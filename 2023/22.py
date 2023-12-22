#!/usr/bin/env python3.12

import aocutils as u
from sys import argv


def main(file: str) -> None:
    print('Day 22')

    bricks = u.input_as_lines(file, map=lambda l: u.double_sep(
        l, '~', ',', map=int, group=tuple))

    bricks.sort(key=lambda b: b[0][2])
    XY = u.defaultdict(int)
    B = {}
    supported_by = u.defaultdict(set)
    supports = u.defaultdict(set)
    for i, [(x1, y1, z1), (x2, y2, z2)] in enumerate(bricks):
        i = chr(i + ord('A'))
        dx, dy, dz = x2 - x1, y2 - y1, z2 - z1
        print(x1, y1, z1, x2, y2, z2, dx, dy, dz)
        m = 0
        for dx in range(x1, x2 + 1):
            for dy in range(y1, y2 + 1):
                m = max(m, XY[(dx, dy)])
        for dx in range(x1, x2 + 1):
            for dy in range(y1, y2 + 1):
                XY[(dx, dy)] = m + z2 - z1 + 1
        for dx in range(x1, x2 + 1):
            for dy in range(y1, y2 + 1):
                B[(dx, dy, XY[(dx, dy)])] = i
        for dx in range(x1, x2 + 1):
            for dy in range(y1, y2 + 1):
                if (dx, dy, XY[(dx, dy)] - 1) in B:
                    supported_by[i].add(B[(dx, dy, XY[(dx, dy)] - 1)])
                    supports[B[(dx, dy, XY[(dx, dy)] - 1)]].add(i)

    print(XY)
    print(B)
    print(supported_by)
    print(supports)


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '22.in'
    main(file)
