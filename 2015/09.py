#!/usr/bin/env python3.12

from sys import argv

import aocutils as u

every = []


def dfs(graph: dict[str, dict[str, int]], visited: set, place: str, dist: int):
    if len(visited) == len(graph):
        every.append(dist)
        return dist

    dists = []
    for path in graph[place]:
        if path in visited:
            continue
        v = visited.copy()
        v.add(path)
        d = dfs(graph, v, path, dist + graph[place][path])
        dists.append(d)
    if not dists:
        return None
    return min(dists)


def main(file: str) -> None:
    print('Day 09')

    data = u.input_as_lines(file, map=str.split)

    graph = u.defaultdict(dict)
    for [p1, _, p2, _, d] in data:
        graph[p1][p2] = int(d)
        graph[p2][p1] = int(d)

    p1 = min(dfs(graph, set([place]), place, 0) for place in graph)
    print(f'{p1=}')

    p2 = sorted(every)[-1]
    print(f'{p2=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '09.in'
    main(file)
