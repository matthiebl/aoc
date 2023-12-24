#!/usr/bin/env python3.12

import aocutils as u
from sys import argv

DIRS = {
    '^': [(0, -1)],
    '>': [(1, 0)],
    'v': [(0, 1)],
    '<': [(-1, 0)],
    '.': u.DXY,
}


def main(file: str) -> None:
    print('Day 23')

    grid = u.input_as_lines(file)
    start = (1, 0)
    finish = (len(grid[0]) - 2, len(grid) - 1)

    G = u.graph_from_grid(grid, '.^>v<')

    nodes = [n for n in G if len(G[n]) > 2 or len(G[n]) == 1]

    G1 = {n: {} for n in nodes}
    G2 = {n: {} for n in nodes}

    def adjacency_list(n, is_p1):
        S = [(n, 0)]
        V = {n}
        while S:
            (x, y), d = S.pop()

            if d > 0 and (x, y) in nodes:
                if is_p1:
                    G1[n][(x, y)] = d
                else:
                    G2[n][(x, y)] = d
                continue

            dirs = DIRS[grid[y][x]] if is_p1 else u.DXY
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if u.in_grid(grid, ny, nx) and grid[ny][nx] != '#' and (nx, ny) not in V:
                    S.append(((nx, ny), d + 1))
                    V.add((nx, ny))

    for n in nodes:
        adjacency_list(n, True)
        adjacency_list(n, False)

    def solve(G):
        seen = set()

        def longest_path(n, dist):
            if n == finish:
                return dist

            longest = -float('inf')
            seen.add(n)
            for nn, nd in G[n].items():
                if nn not in seen:
                    longest = max(longest, longest_path(nn, dist + nd))
            seen.remove(n)

            return longest

        return longest_path(start, 0)

    p1 = solve(G1)
    print(f'{p1=}')
    p2 = solve(G2)
    print(f'{p2=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '23.in'
    main(file)
