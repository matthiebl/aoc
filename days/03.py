#!/usr/bin/env python3.10

from sys import argv
import advent as adv


def main(file: str) -> None:
    print('Day 03')

    data: list[str] = adv.input_as_lines(file)

    p1 = []
    V = set()

    def find_num(x, y):
        if (x, y) in V:
            return
        if x < 0 or y < 0:
            return
        if x >= len(data[0]) or y >= len(data):
            return

        if data[y][x] not in '0987654321':
            return
        while x > 0 and data[y][x] in '0987654321':
            x -= 1
        if data[y][x] not in '0987654321':
            x += 1
        if (x, y) in V:
            return

        n = 0
        V.add((x, y))
        while x < len(data[0]):
            c = data[y][x]
            if c not in '0987654321':
                p1.append(n)
                return
            n *= 10
            n += int(c)
            x += 1
        p1.append(n)

    p2 = []
    for y, row in enumerate(data):
        for x, c in enumerate(row):
            if c in '1234567890.':
                continue
            l1 = len(p1)
            find_num(x - 1, y - 1)
            find_num(x - 1, y)
            find_num(x - 1, y + 1)
            find_num(x, y - 1)
            find_num(x, y + 1)
            find_num(x + 1, y - 1)
            find_num(x + 1, y)
            find_num(x + 1, y + 1)
            l2 = len(p1)
            if c == '*' and l2 - l1 == 2:
                a = p1[-1]
                b = p1[-2]
                p2.append(a * b)
    print(sum(p1))
    print(sum(p2))


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '03.in'
    main(file)
