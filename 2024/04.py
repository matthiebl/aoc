#!/usr/bin/env python3.12

from sys import argv

import aocutils as u


def main(file: str) -> None:
    print('Day 04')

    data = u.input_as_lines(file)

    p1 = 0
    # Horizontals
    for y in range(len(data)):
        for x in range(len(data[0]) - 3):
            search = data[y][x:x+4]
            if search in ['XMAS', 'SAMX']:
                p1 += 1
    # Verticals
    for y in range(len(data) - 3):
        for x in range(len(data[0])):
            search = data[y][x] + data[y+1][x] + data[y+2][x] + data[y+3][x]
            if search in ['XMAS', 'SAMX']:
                p1 += 1
    # Diagonals
    for y in range(len(data) - 3):
        for x in range(len(data[0]) - 3):
            search = data[y][x] + data[y+1][x+1] + data[y+2][x+2] + data[y+3][x+3]
            if search in ['XMAS', 'SAMX']:
                p1 += 1
            search = data[y+3][x] + data[y+2][x+1] + data[y+1][x+2] + data[y][x+3]
            if search in ['XMAS', 'SAMX']:
                p1 += 1
    print(f'{p1=}')

    p2 = 0
    for y in range(len(data) - 2):
        for x in range(len(data) - 2):
            down = data[y][x] + data[y+1][x+1] + data[y+2][x+2]
            up = data[y+2][x] + data[y+1][x+1] + data[y][x+2]
            if down in ['MAS', 'SAM'] and up in ['MAS', 'SAM']:
                p2 += 1

    print(f'{p2=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '04.in'
    main(file)
