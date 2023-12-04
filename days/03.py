#!/usr/bin/env python3.10

from sys import argv
import advent as adv


def main(file: str) -> None:
    print('Day 03')

    data: list[str] = adv.input_as_lines(file)

    p1 = []
    V = set()

    def add_num(x, y):
        if x < 0 or y < 0 or x >= len(data[0]) or y >= len(data):
            return
        if data[y][x] not in '1234567890':
            return
        # here coord is valid number

        while x > 0 and data[y][x] in '1234567890':
            x -= 1
        if data[y][x] not in '1234567890':
            x += 1
        # at most significant number, so check if found else add it
        if (x, y) in V:
            return
        V.add((x, y))

        n = ''
        while x < len(data[0]) and data[y][x] in '1234567890':
            n += data[y][x]
            x += 1
        p1.append(int(n))

    p2 = 0
    for y, row in enumerate(data):
        for x, c in enumerate(row):
            if c in '1234567890.':
                continue
            # only care about parts
            l1 = len(p1)
            for xx in [-1, 0, 1]:
                for yy in [-1, 0, 1]:
                    add_num(x + xx, y + yy)
            l2 = len(p1)
            if c == '*' and l2 - l1 == 2:
                p2 += p1[-1] * p1[-2]

    print('p1=' + str(sum(p1)))
    print(f'{p2=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '03.in'
    main(file)
