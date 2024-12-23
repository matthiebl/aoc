"""
--- Day 23: LAN Party ---
https://adventofcode.com/2024/day/23
"""

import networkx as nx
from utils import *

args = parse_args(year=2024, day=23)
raw = get_input(args.filename, year=2024, day=23)

lines = raw.splitlines()

G = nx.Graph()
for line in lines:
    a, b = line.split("-")
    G.add_nodes_from((a, b))
    G.add_edge(a, b)

complete_subgraphs = list(nx.enumerate_all_cliques(G))

p1 = sum(1 for nodes in complete_subgraphs if len(nodes) == 3 and sum(1 for n in nodes if n.startswith("t")) >= 1)
print(p1)

p2 = ",".join(sorted(complete_subgraphs[-1]))
print(p2)

if args.test:
    args.tester(p1, p2)
