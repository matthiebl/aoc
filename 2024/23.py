"""
--- Day 23: LAN Party ---
https://adventofcode.com/2024/day/23

For this problem, we want to find subgraphs of the graph that are complete graphs, which are also known as
cliques (https://en.wikipedia.org/wiki/Clique_(graph_theory)). For this we already have the networkx package
that handles this problem for us in `enumerate_all_cliques`.

For part one we just need all the cliques of length 3, and for part two the longest.
"""

from networkx import from_edgelist, enumerate_all_cliques
from utils import *

args = parse_args(year=2024, day=23)
raw = get_input(args.filename, year=2024, day=23)

edges = [tuple(line.split("-")) for line in raw.splitlines()]

graph = from_edgelist(edges)
complete_subgraphs = list(enumerate_all_cliques(graph))

p1 = sum(1 for nodes in complete_subgraphs if len(nodes) == 3 and sum(1 for n in nodes if n.startswith("t")) >= 1)
p2 = ",".join(sorted(complete_subgraphs[-1]))

print(p1)
print(p2)

if args.test:
    args.tester(p1, p2)
