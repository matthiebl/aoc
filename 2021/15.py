#!/usr/bin/env python3.12

import aocutils as u
from sys import argv

from heapq import heappush, heappop


def main(file: str) -> None:
    print('Day 15')

    grid = u.input_as_lines(file)

    H = len(grid)
    W = len(grid[0])

    def value(x: int, y: int) -> int:
        val = int(grid[y % H][x % W])
        for _ in range(x // W + y // H):
            val += 1
            if val == 10:
                val = 1
        return val

    def dijkstras(X: int, Y: int) -> int:
        pq = [(0, 0, 0)]
        visited = {(0, 0)}
        while pq:
            dist, x, y = heappop(pq)

            if (x, y) == (X - 1, Y - 1):
                return dist

            for dx, dy in u.DXY:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < X and 0 <= ny < Y and (nx, ny) not in visited:
                    heappush(pq, (dist + value(nx, ny), nx, ny))
                    visited.add((nx, ny))

    d = dijkstras(W, H)
    print(d)
    d = dijkstras(W * 5, H * 5)
    print(d)

    # hi 2948


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '15.in'
    main(file)
