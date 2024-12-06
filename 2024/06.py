#!/usr/bin/env python3.12

from sys import argv

import aocutils as u

D = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def find_guard(grid: list[list[int]]) -> tuple[int, int]:
    for r, row in enumerate(grid):
        if '^' in row:
            return (r, row.index('^'))
    raise RuntimeError('Could not find guard `^`')


def traverse_grid(grid: list[list[int]], start: tuple[int, int]) -> set[tuple[int, int]]:
    R = len(grid)
    C = len(grid[0])
    path = set([start])
    r, c = start
    d = 0  # index in D
    while True:
        dr, dc = D[d % len(D)]
        nr, nc = r + dr, c + dc
        if not (0 <= nr < R and 0 <= nc < C):
            return path
        if grid[nr][nc] == '#':
            d += 1
        else:
            r, c = nr, nc
        path.add((r, c))


def is_loop(grid: list[list[int]], start: tuple[int, int]) -> bool:
    R = len(grid)
    C = len(grid[0])
    turns = set()
    r, c = start
    d = 0
    while True:
        dr, dc = D[d % len(D)]
        nr, nc = r + dr, c + dc
        if not (0 <= nr < R and 0 <= nc < C):
            return False
        if grid[nr][nc] == '#':
            if (r, c, d % len(D)) in turns:
                return True
            turns.add((r, c, d % len(D)))
            d += 1
        else:
            r, c = nr, nc


def main(file: str) -> None:
    print('Day 06')

    grid = [list(l) for l in u.input_as_lines(file)]

    guard = find_guard(grid)

    path = traverse_grid(grid, guard)
    p1 = len(path)
    print(f'{p1=}')

    p2 = 0
    for r, c in path:
        if grid[r][c] != '.':
            continue
        grid[r][c] = '#'
        if is_loop(grid, guard):
            p2 += 1
        grid[r][c] = '.'
    print(f'{p2=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '06.in'
    main(file)
