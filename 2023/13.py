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


def find_reflection_score(space, exclude: int = 0):
    for i in range(1, len(space)):
        score = 100 * reflection_h(space, i)
        if score > 0 and score != exclude:
            return score
    rotated = rotate(space)
    for i in range(1, len(rotated)):
        score = reflection_h(rotated, i)
        if score > 0 and score != exclude:
            return score
    return 0


def smudge_score(space, prev_score: int):
    for i in range(len(space)):
        for j in range(len(space[i])):
            space[i] = list(space[i])
            space[i][j] = '#' if space[i][j] == '.' else '.'
            space[i] = ''.join(space[i])

            new_score = find_reflection_score(space, prev_score)
            if new_score:
                return new_score

            space[i] = list(space[i])
            space[i][j] = '#' if space[i][j] == '.' else '.'
            space[i] = ''.join(space[i])


def main(file: str) -> None:
    print('Day 13')

    spaces = u.input_from_grouped_lines(file)

    p1 = 0
    p2 = 0
    for space in spaces:
        score = find_reflection_score(space)
        p1 += score
        p2 += smudge_score(space, score)

    print(f'{p1=}')
    print(f'{p2=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '13.in'
    main(file)
