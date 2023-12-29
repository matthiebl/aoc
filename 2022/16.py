#!/usr/bin/env python3.12

import aocutils as u
from sys import argv

from collections import deque
from functools import cache


def main(file: str) -> None:
    print('Day 16')

    valves: dict[str, int] = {}
    tunnels: dict[str, list[str]] = {}

    data = u.input_as_lines(file)
    for line in data:
        valve = line[6:8]
        valves[valve] = int(line[23:line.find(';')])
        leads_to = [to[-2:] for to in line.split(', ')]
        tunnels[valve] = leads_to

    dists: dict[str, dict[str, int]] = {}
    index: dict[str, int] = {}

    # find the connection from non-zero flow valves
    # to other non-zero flow nodes
    # to help skip pointless nodes
    for valve in valves:
        if valve != 'AA' and valves[valve] == 0:
            continue

        # set up indecies to speed up bit masking
        if valve != 'AA':
            index[valve] = len(index)

        dists[valve] = {valve: 0, 'AA': 0}

        queue = deque([(0, valve)])
        visited = {valve}

        while queue:
            dist, pos = queue.popleft()
            for neighbour in tunnels[pos]:
                if neighbour in visited:
                    continue
                visited.add(neighbour)
                if valves[neighbour]:
                    dists[valve][neighbour] = dist + 1
                queue.append((dist + 1, neighbour))

        del dists[valve][valve]
        if 'AA' in dists[valve]:
            del dists[valve]['AA']

    @cache  # cache to reduce double counting
    def traverse(time: int, valve: str, opened: int):
        best = 0

        # traverse neighbours first to skip wasting time on 'AA'
        for neighbour in dists[valve]:
            # check if opened before
            if opened & (1 << index[neighbour]):
                continue

            remaining_time = time - dists[valve][neighbour] - 1
            if remaining_time <= 0:
                continue

            # work out best time for each neighbour
            flow = valves[neighbour] * remaining_time
            traverse_best = traverse(remaining_time, neighbour,
                                     opened | (1 << index[neighbour]))
            best = max(best, flow + traverse_best)

        return best

    p1 = traverse(30, 'AA', 0)
    print(f'{p1=}')

    p2 = 0
    opened = (1 << len(index)) - 1
    for i in range(opened + 1):
        p2 = max(p2, traverse(26, 'AA', i) + traverse(26, 'AA', opened ^ i))
    print(f'{p2=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '16.in'
    main(file)
