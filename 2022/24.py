#!/usr/bin/env python3.12

import aocutils as u
from sys import argv


def main(file: str) -> None:
    print('Day 24')

    data = u.input_as_lines(file)

    ROWS = len(data)
    COLS = len(data[0])

    def move_tornado(d: tuple, p: tuple):
        x, y = p
        dx, dy = d
        x, y = x + dx, y + dy
        if x == 0 or x == COLS - 1:
            x = abs(COLS - 2 - x)
        if y == 0 or y == ROWS - 1:
            y = abs(ROWS - 2 - y)
        return (x, y)

    every = set()
    tornados = {'>': set(), 'v': set(), '<': set(), '^': set()}
    D = {'>': (1, 0), 'v': (0, 1), '<': (-1, 0), '^': (0, -1)}
    for y, row in enumerate(data):
        for x, ch in enumerate(row):
            if ch in tornados:
                tornados[ch].add((x, y))
            if ch in '<^>v.':
                every.add((x, y))

    clear = []

    for t in range(900):
        comb = tornados['<'].union(tornados['^']).union(
            tornados['>']).union(tornados['v'])
        clear.append(every - comb)

        new_tornados = {'>': set(), 'v': set(), '<': set(), '^': set()}
        for d, tornado_set in tornados.items():
            for tornado in tornado_set:
                new_tornados[d].add(move_tornado(D[d], tornado))
        tornados = new_tornados

    def bfs(start: tuple, end: tuple, time: int = 0, round: int = 0):
        V = set()
        Q = [(*start, time)]
        while len(Q) > 0:
            x, y, t = Q.pop(0)
            if (x, y, t) in V:
                continue
            V.add((x, y, t))

            if (x, y) == end:
                if round == 0:
                    return t
                return bfs((x, y), start, t, round - 1)

            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1), (0, 0)]:
                if (x + dx, y + dy) in clear[t + 1]:
                    Q.append((x + dx, y + dy, t + 1))

    p1 = bfs((1, 0), (COLS - 2, ROWS - 1))
    print(f'{p1=}')

    p2 = bfs((1, 0), (COLS - 2, ROWS - 1), round=2)
    print(f'{p2=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '24.in'
    main(file)
