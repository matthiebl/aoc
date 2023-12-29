#!/usr/bin/env python3.12

import aocutils as u
from sys import argv


def main(file: str) -> None:
    print('Day 05')

    lines = u.input_as_lines(file, map=u.find_digits)

    points = u.defaultdict(int)
    points2 = u.defaultdict(int)

    for x1, y1, x2, y2 in lines:
        (x1, y1), (x2, y2) = sorted([(x1, y1), (x2, y2)])

        if x1 == x2 or y1 == y2:
            for xx in range(x1, x2+1):
                for yy in range(y1, y2+1):
                    points[(xx, yy)] += 1
                    points2[(xx, yy)] += 1
        else:
            dx, dy = (1, -1) if y2 < y1 else (1, 1)
            xx, yy = x1, y1
            points2[(xx, yy)] += 1
            while (xx, yy) != (x2, y2):
                xx += dx
                yy += dy
                points2[(xx, yy)] += 1

    p1 = sum(1 if v > 1 else 0 for v in points.values())
    print(f'{p1=}')
    p2 = sum(1 if v > 1 else 0 for v in points2.values())
    print(f'{p2=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '05.in'
    main(file)
