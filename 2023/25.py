"""
--- Day 25: Snowverload ---
https://adventofcode.com/2023/day/25
"""

from networkx import Graph, connected_components, minimum_edge_cut

from utils import *

args = parse_args(year=2023, day=25)
raw = get_input(args.filename, year=2023, day=25)

edges = flatmap([[(n1, n2) for n2 in lst.split()] for n1, lst in [line.split(": ") for line in raw.splitlines()]])

graph = Graph()
graph.add_edges_from(edges)

graph.remove_edges_from(minimum_edge_cut(graph))
forests = connected_components(graph)

p1 = len(next(forests)) * len(next(forests))
print(p1)

p2 = None
print(p2)

if args.test:
    args.tester(p1, p2)
