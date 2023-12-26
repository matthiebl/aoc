#!/usr/bin/env python3.12

import aocutils as u
from sys import argv


def main(file: str) -> None:
    print('Day 8')

    trees = u.input_as_lines(file)

    ROWS = len(trees)
    COLS = len(trees[0])

    def isVisible(r, c):
        if r == 0 or r == ROWS - 1 or c == 0 or c == COLS - 1:
            return True

        val = trees[r][c]
        for ri in range(r+1):
            if ri == r:
                return True
            if trees[ri][c] >= val:
                break
        for ri in range(ROWS-1, r-1, -1):
            if ri == r:
                return True
            if trees[ri][c] >= val:
                break
        for ci in range(c+1):
            if ci == c:
                return True
            if trees[r][ci] >= val:
                break
        for ci in range(COLS-1, c-1, -1):
            if ci == c:
                return True
            if trees[r][ci] >= val:
                break
        return False

    p1 = 0
    for r in range(ROWS):
        for c in range(COLS):
            if isVisible(r, c):
                p1 += 1
    print(f'{p1=}')

    def scenicScore(r, c):
        val = trees[r][c]

        left = 0
        for ri in range(r-1, -1, -1):
            left += 1
            if trees[ri][c] >= val:
                break

        right = 0
        for ri in range(r+1, ROWS):
            right += 1
            if trees[ri][c] >= val:
                break

        up = 0
        for ci in range(c-1, -1, -1):
            up += 1
            if trees[r][ci] >= val:
                break

        down = 0
        for ci in range(c+1, COLS):
            down += 1
            if trees[r][ci] >= val:
                break

        return left * right * up * down

    scores = []
    for r in range(ROWS):
        for c in range(COLS):
            scores.append(scenicScore(r, c))
    p2 = max(scores)
    print(f'{p2=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '08.in'
    main(file)
