"""
--- Day 24: Crossed Wires ---
https://adventofcode.com/2024/day/24
"""

import networkx as nx
from utils import *

args = parse_args(year=2024, day=24)
raw = get_input(args.filename, year=2024, day=24)

lines = raw.splitlines()

initial, connections = [group.splitlines() for group in raw.split("\n\n")]

values = {}
for line in initial:
    wire, value = line.split(": ")
    values[wire] = int(value)

graph = nx.DiGraph()
wires = {}
for wire in connections:
    rule, out = wire.split(" -> ")
    wires[out] = rule.split(" ")
    graph.add_nodes_from([(out, {"name": out, "operation": wires[out][1]})])
    graph.add_edge(out, wires[out][0])
    graph.add_edge(out, wires[out][2])


def value_of(wire):
    if wire in values:
        return values[wire]
    
    rules = wires[wire]
    if rules[1] == "AND":
        val = value_of(rules[0]) & value_of(rules[2])
    elif rules[1] == "OR":
        val = value_of(rules[0]) | value_of(rules[2])
    elif rules[1] == "XOR":
        val = value_of(rules[0]) ^ value_of(rules[2])
    
    values[wire] = val
    return val


p1 = 0
p2 = 0

bits = []
for wire in wires:
    if wire[0] == "z":
        bits.append((wire, value_of(wire)))
p1 = int("".join(map(str, [b for _, b in sorted(bits, reverse=True)])), 2)
print(p1)

# nx.write_graphml(graph, "static/graph.xml")

# print(p2)

if args.test:
    args.tester(p1, p2)
