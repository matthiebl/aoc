#!/usr/bin/env python3.10

from sys import argv, setrecursionlimit
import advent as adv

setrecursionlimit(10000)

help_me = {
    ('|', 0, 1): (1, 0, -1, 0),
    ('|', 0, -1): (-1, 0, 1, 0),
    ('-', 1, 0): (0, -1, 0, 1),
    ('-', -1, 0): (0, 1, 0, -1),
    ('L', 1, 0): (0, 0, 0, 1),
    ('L', 0, -1): (-1, 0, 0, 0),
    ('J', -1, 0): (0, 1, 0, 0),
    ('J', 0, -1): (0, 0, 1, 0),
    ('F', 0, 1): (0, 0, -1, 0),
    ('F', 1, 0): (-1, 0, 0, 0),
    ('7', -1, 0): (0, 0, 0, -1),
    ('7', 0, 1): (1, 0, 0, 0),
}


def valid(data, x, y):
    if 0 <= x < len(data[0]) and 0 <= y < len(data):
        return True
    return False


def find_all(data, G, V, x, y):
    if not valid(data, x, y) or (x, y) in G:
        return
    q = [(x, y)]
    while q:
        x, y = q.pop(0)
        if (x, y) in V:
            continue
        V.add((x, y))

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if valid(data, x + dx, y + dy) and (x + dx, y + dy) not in G:
                q.append((x + dx, y + dy))


def main(file: str) -> None:
    print('Day 10')

    data = [list(row) for row in adv.input_as_lines(file)]

    # setup
    G: dict[tuple[int, int], list[tuple[int, int]]] = {}
    start = None
    for y, row in enumerate(data):
        for x, i in enumerate(row):
            if i == 'L':
                G[(x, y)] = [(x + 1, y), (x, y - 1)]
            if i == 'J':
                G[(x, y)] = [(x - 1, y), (x, y - 1)]
            if i == 'F':
                G[(x, y)] = [(x + 1, y), (x, y + 1)]
            if i == '7':
                G[(x, y)] = [(x - 1, y), (x, y + 1)]
            if i == '|':
                G[(x, y)] = [(x, y - 1), (x, y + 1)]
            if i == '-':
                G[(x, y)] = [(x - 1, y), (x + 1, y)]

            if i == 'S':
                start = (x, y)
                G[start] = []
                t, b, l, r = None, None, None, None
                if data[y - 1][x] in '|7F':
                    G[start].append((x, y - 1))
                    t = True
                if data[y + 1][x] in '|JL':
                    G[start].append((x, y + 1))
                    b = True
                if data[y][x - 1] in 'LF-':
                    G[start].append((x - 1, y))
                    l = True
                if data[y][x + 1] in '7J-':
                    G[start].append((x + 1, y))
                    r = True
                if t and r:
                    data[y][x] = 'L'
                if t and l:
                    data[y][x] = 'J'
                if b and r:
                    data[y][x] = 'F'
                if b and l:
                    data[y][x] = '7'

    # p1 logic
    V = set()
    p1 = 0
    queue = [(start, 0)]
    while queue:
        (n, d) = queue.pop(0)
        if n in V or n not in G:
            continue
        V.add(n)

        p1 = max(p1, d)
        for coord in G[n]:
            queue.append((coord, d + 1))
    print(f'{p1=}')

    # p2 logic
    LEFT = set()
    RIGHT = set()
    V2 = set()
    x, y = start
    dx, dy = (-1, 0)
    if data[y][x] in 'LF':
        dx, dy = (1, 0)
    while (x, y) not in V2:
        V2.add((x, y))

        ans = help_me.get((data[y][x], dx, dy), None)
        if ans is not None:
            dxl, dyl, dxr, dyr = ans
            find_all(data, V, LEFT, x + dxl, y + dyl)
            find_all(data, V, RIGHT, x + dxr, y + dyr)

        x, y = x + dx, y + dy
        a, b = G[(x, y)]
        nx, ny = a if b in V2 else b
        dx, dy = nx - x, ny - y

    # p2 with either be on the left or right of the loop
    print(len(LEFT))
    print(len(RIGHT))
    # too lazy to work out which side


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '10.in'
    main(file)
