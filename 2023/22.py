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
    below = u.defaultdict(set)
    above = u.defaultdict(set)

    # Did this sort of inefficiently, but sort of logically.
    for i, [(x1, y1, z1), (x2, y2, z2)] in enumerate(bricks):
        dx, dy, dz = x2 - x1, y2 - y1, z2 - z1
        # Find the (m)ax height of a placed
        # brick below the current brick at each (x,y)
        m = 0
        for dx in range(x1, x2 + 1):
            for dy in range(y1, y2 + 1):
                m = max(m, XY[(dx, dy)])
        # Update max height at (x,y),
        # then place the current brick at that height
        for dx in range(x1, x2 + 1):
            for dy in range(y1, y2 + 1):
                XY[(dx, dy)] = m + z2 - z1 + 1
        for dx in range(x1, x2 + 1):
            for dy in range(y1, y2 + 1):
                for dz in range(z2 - z1 + 1):
                    B[(dx, dy, XY[(dx, dy)] - dz)] = i
        # Then check for all the bricks below the current brick,
        # as well as the reverse
        for dx in range(x1, x2 + 1):
            for dy in range(y1, y2 + 1):
                for dz in range(z2 - z1 + 1):
                    if (dx, dy, XY[(dx, dy)] - dz - 1) in B:
                        below[i].add(B[(dx, dy, XY[(dx, dy)] - dz - 1)])
                        above[B[(dx, dy, XY[(dx, dy)] - dz - 1)]].add(i)
    # This leaves multi-height bricks having themselves in these lists,
    # but we can compensate for that

    def disolvable(brick):
        s1 = above[brick] - {brick}
        for b in s1:
            s2 = below[b] - {brick, b}
            if len(s2) == 0:
                return False
        return True

    p1 = 0
    for brick in range(len(bricks)):
        if disolvable(brick):
            p1 += 1
    print(f'{p1=}')

    def fall(brick) -> int:
        fallen = set()
        check = [brick]
        while check:
            this_brick = check.pop(0)
            if this_brick in fallen:
                continue
            fallen.add(this_brick)

            s = above[this_brick] - {this_brick}
            for b in s:
                s2 = below[b] - {b} - fallen
                if len(s2) == 0:
                    check.append(b)
        return len(fallen) - 1

    p2 = 0
    for brick in range(len(bricks)):
        p2 += fall(brick)
    print(f'{p2=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '22.in'
    main(file)
