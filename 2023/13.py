#!/usr/bin/env python3.12

import aocutils as u
from sys import argv


def rotate(lst):
    return [''.join(c) for c in zip(*lst[::-1])]


def reflection_h(space, row):
    above = space[:row]
    above.reverse()
    below = space[row:]

    for a, b in zip(above, below):
        if a != b:
            return 0
    return row


def reflection_v(space, row):
    space = rotate(space)
    above = space[:row]
    above.reverse()
    below = space[row:]

    for a, b in zip(above, below):
        if a != b:
            return 0
    return row


def main(file: str) -> None:
    print('Day 13')

    spaces = u.input_from_grouped_lines(file)

    p1 = 0
    p2 = 0
    for space in spaces:
        score = 0
        for i in range(1, len(space)):
            score += 100 * reflection_h(space, i)
        rotated = rotate(space)
        for i in range(1, len(rotated)):
            score += reflection_h(rotated, i)
        p1 += score

        new = 0
        found = False
        for i in range(len(space)):
            if found:
                break
            for j in range(len(space[i])):
                if found:
                    break

                space[i] = list(space[i])
                space[i][j] = '#' if space[i][j] == '.' else '.'
                space[i] = ''.join(space[i])

                for k in range(1, len(space)):
                    new = 100 * reflection_h(space, k)
                    if new == score:
                        new = 0
                    if new:
                        found = True
                        p2 += new
                        break
                rotated = rotate(space)
                for k in range(1, len(rotated)):
                    new = reflection_h(rotated, k)
                    if new == score:
                        new = 0
                    if new:
                        found = True
                        p2 += new
                        break

                space[i] = list(space[i])
                space[i][j] = '#' if space[i][j] == '.' else '.'
                space[i] = ''.join(space[i])

    print(f'{p1=}')
    print(f'{p2=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '13.in'
    main(file)
