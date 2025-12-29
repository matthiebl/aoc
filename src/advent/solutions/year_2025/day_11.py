"""
--- Day 11: Reactor ---
https://adventofcode.com/2025/day/11

Relies on the fact that the graph is acyclical.

Confirmed via visulisation of nx.write_graphml -> https://www.yworks.com/yed-live/
"""

from collections import defaultdict
from functools import cache
from pathlib import Path

import networkx as nx

from advent.core import Solver


class Day11(Solver):
    """Solution for day 11."""

    SERVER = "svr"
    YOU = "you"
    OUT = "out"

    def prepare(self) -> None:
        self.store.graph = defaultdict(list)
        for line in self.input.lines():
            src, to = line.split(": ")
            self.store.graph[src] = to.split()

    def part1(self) -> int:
        """Solve part 1."""
        return self.topological_paths(self.YOU, self.OUT, tuple())

    def part2(self) -> int:
        """Solve part 2."""
        return self.topological_paths(self.SERVER, self.OUT, ("dac", "fft"))

    @cache
    def topological_paths(self, src: str, dst: str, passed: tuple[str]) -> int:
        if src == dst:
            return 1 if not len(passed) else 0

        if src in passed:
            passed = tuple(set(passed) - set((src,)))

        return sum(self.topological_paths(adj, dst, passed) for adj in self.store.graph[src])

    def save_to_graphml(self):
        # Create networkx graph
        G = nx.Graph()
        for src, neighbours in self.store.graph.items():
            G.add_node(src, data=src)
            for adj in neighbours:
                G.add_edge(src, adj)

        # Save to graphml to be loaded in https://www.yworks.com/yed-live/
        path = self.solution_dir.joinpath("day_11_graph.graphml")
        nx.write_graphml(G, path)
