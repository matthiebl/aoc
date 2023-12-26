#!/usr/bin/env python3.12

import aocutils as u
from sys import argv


def main(file: str) -> None:
    print('Day 12')

    height_map = u.input_as_lines(file)

    ROWS = len(height_map)
    COLS = len(height_map[0])

    H = list('SabcdefghijklmnopqrstuvwxyzE')
    S = None
    for r, row in enumerate(height_map):
        try:
            s = row.index('S')
            S = (r, s)
        except:
            pass

    def bfs(S):
        V = set()
        queue = [(0, S)]
        while queue:
            dist, (r, c) = queue.pop(0)
            h = H.index(height_map[r][c])
            V.add((r, c))

            if H[h] == 'E':
                return dist

            for dr, dc in u.DXY:
                nr, nc = r + dr, c + dc
                if u.in_grid(height_map, nr, nc) and (nr, nc) not in V and height_map[nr][nc] in H[:h+2]:
                    queue.append((dist + 1, (nr, nc)))
                    V.add((nr, nc))
    p1 = bfs(S)
    print(f'{p1=}')

    dists = [p1]
    for r, row in enumerate(height_map):
        for c, col in enumerate(row):
            if col == 'a':
                dist = bfs((r, c))
                if dist:
                    dists.append(dist)
    dists.sort()
    p2 = dists[0]
    print(f'{p2=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '12.in'
    main(file)
