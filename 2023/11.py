#!/usr/bin/env python3.12

from sys import argv
import aocutils as u


def rotate(lst):
    return [list(c) for c in zip(*lst[::-1])]


def smart_expand(data: list[list[str]]) -> list[list[str]]:
    rows = []
    i = 0
    for row in data:
        if row.count('#') == 0:
            i += 1
        rows.append(i)

    rotated = rotate(data)
    cols = []
    i = 0
    for row in rotated:
        if row.count('#') == 0:
            i += 1
        cols.append(i)

    return rows, cols


def total_dist_expanded(galaxies: list[tuple[int, int]], rows: list[int], cols: list[int], multiplier: int):
    total = 0
    for i, (x1, y1) in enumerate(galaxies):
        for (x2, y2) in galaxies[i:]:
            n_x1 = x1 + cols[x1] * multiplier
            n_x2 = x2 + cols[x2] * multiplier
            n_y1 = y1 + rows[y1] * multiplier
            n_y2 = y2 + rows[y2] * multiplier
            dist = abs(n_x2 - n_x1) + abs(n_y2 - n_y1)
            total += dist
    return total


def main(file: str) -> None:
    print('Day 11')

    data = [list(row) for row in u.input_as_lines(file)]

    galaxies = []
    for y, row in enumerate(data):
        for x, it in enumerate(row):
            if it == '#':
                galaxies.append((x, y))

    rows, cols = smart_expand(data)

    p1 = total_dist_expanded(galaxies, rows, cols, 1)
    print(f'{p1=}')

    p2 = total_dist_expanded(galaxies, rows, cols, 1000000 - 1)
    print(f'{p2=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '11.in'
    main(file)
