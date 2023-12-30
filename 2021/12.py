#!/usr/bin/env python3.12

import aocutils as u
from sys import argv


def main(file: str) -> None:
    print('Day 12')

    edges = u.input_as_lines(file)

    G = u.defaultdict(list)
    visited = {}

    for edge in edges:
        a, b = edge.split('-')
        G[a].append(b)
        G[b].append(a)
        visited[a] = 1000
        visited[b] = 1000

    for v in visited:
        if v.lower() == v:
            visited[v] = 1
    visited['start'] = 0

    def dfs(node: str, visited: dict[str, int], double: bool = True):
        if node == 'end':
            return 1
        finish = 0
        for adj in G[node]:
            if visited[adj] > 0:
                copy = dict(visited)
                copy[adj] -= 1
                finish += dfs(adj, copy, double)
            elif adj.lower() == adj and adj not in ['start', 'end'] and not double:
                finish += dfs(adj, visited, True)
        return finish

    copy = dict(visited)
    p1 = dfs('start', visited)
    print(f'{p1=}')

    p2 = dfs('start', copy, False)
    print(f'{p2=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '12.in'
    main(file)
