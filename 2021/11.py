#!/usr/bin/env python3.12

import aocutils as u
from sys import argv


def main(file: str) -> None:
    print('Day 11')

    octopus = u.input_as_lines(file, map=lambda l: u.map_int(list(l)))

    def step():
        to_flash = []
        for r, row in enumerate(octopus):
            for c, octo in enumerate(row):
                octopus[r][c] += 1
                if octo + 1 > 9:
                    to_flash.append((r, c))
        flashed = set(to_flash)
        while to_flash:
            r, c = to_flash.pop()
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    nr = r + dr
                    nc = c + dc
                    if u.in_grid(octopus, nr, nc) and (nr, nc) not in flashed:
                        octopus[nr][nc] += 1
                        if octopus[nr][nc] > 9:
                            to_flash.append((nr, nc))
                            flashed.add((nr, nc))

        for r, c in flashed:
            octopus[r][c] = 0
        return len(flashed)

    p1 = 0
    for _ in range(100):
        p1 += step()
    print(f'{p1=}')

    flashed = 0
    target = len(octopus) * len(octopus[0])

    p2 = 100
    while flashed != target:
        flashed = step()
        p2 += 1
    print(f'{p2=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '11.in'
    main(file)
