#!/usr/bin/env python3.12

import aocutils as u
from sys import argv

import networkx as nx


def main(file: str) -> None:
    print('Day 25')

    edges = u.input_as_lines(file)

    G = nx.Graph()
    for line in edges:
        a, lst = line.split(': ')
        lst = lst.split()
        G.add_node(a)
        for b in lst:
            G.add_node(b)
            G.add_edge(a, b)

    G.remove_edges_from(nx.minimum_edge_cut(G))

    forests = nx.connected_components(G)
    p1 = len(next(forests)) * len(next(forests))

    print(f'{p1=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '25.in'
    main(file)
