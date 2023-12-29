#!/usr/bin/env python3.12

import aocutils as u
from sys import argv

import heapq as hq


def main(file: str) -> None:
    print('Day 09')

    cave_floor = u.input_as_lines(file)

    low_points = []

    p1 = 0
    for r, row in enumerate(cave_floor):
        for c, ch in enumerate(row):
            if all(cave_floor[r + dr][c + dc] > ch for dr, dc in u.DXY if u.in_grid(cave_floor, r + dr, c + dc)):
                low_points.append((r, c))
                p1 += 1 + int(ch)
    print(f'{p1=}')

    basin_sizes = []

    for low in low_points:
        stack = [low]
        visited = {low}
        while stack:
            r, c = stack.pop()
            for dr, dc in u.DXY:
                if u.in_grid(cave_floor, r+dr, c + dc) and (r + dr, c + dc) not in visited and cave_floor[r + dr][c+dc] != '9':
                    stack.append((r + dr, c + dc))
                    visited.add((r + dr, c + dc))
        hq.heappush(basin_sizes, -len(visited))

    p2 = -hq.heappop(basin_sizes) * hq.heappop(basin_sizes) * hq.heappop(basin_sizes)
    print(f'{p2=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '09.in'
    main(file)
