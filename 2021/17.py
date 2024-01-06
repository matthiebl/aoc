#!/usr/bin/env python3.12

import aocutils as u
from sys import argv


def main(file: str) -> None:
    print('Day 17')

    x1, x2, y1, y2 = u.find_digits(u.read_input(file))

    p1 = 0
    p2 = 0

    for ux in range(1, x2 + 1):
        for uy in range(y1, -2 * y2 + 2):
            my = 0
            x, y, vx, vy = 0, 0, ux, uy
            while x <= x2 and y >= y1:
                x += vx
                y += vy
                vy -= 1
                vx = max(0, vx - 1)
                my = max(my, y)
                if x1 <= x <= x2 and y1 <= y <= y2:
                    p1 = max(p1, my)
                    p2 += 1
                    break

    print(f'{p1=}')
    print(f'{p2=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '17.in'
    main(file)
