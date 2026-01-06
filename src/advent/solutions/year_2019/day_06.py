"""
--- Day 6: Universal Orbit Map ---
https://adventofcode.com/2019/day/6
"""

from functools import cache

from advent.core import Solver
from advent.utils.graph import Graph


class Day06(Solver):
    """Solution for day 6."""

    ROOT = "COM"
    YOU = "YOU"
    SANTA = "SAN"

    def prepare(self) -> None:
        self.graph = Graph[str]()
        for line in self.input.lines():
            orbits, obj = line.split(")")
            self.graph.add_edge(obj, orbits)

    def part1(self) -> int:
        """Solve part 1."""
        return sum(self.orbits(n) for n in self.graph.nodes)

    def part2(self) -> int:
        """Solve part 2."""
        you_chain = self.orbit_chain(self.YOU)
        santa_chain = self.orbit_chain(self.SANTA)
        while you_chain.pop() == santa_chain.pop():
            continue
        return len(you_chain) + len(santa_chain)

    @cache
    def orbits(self, object: str) -> int:
        if object == self.ROOT:
            return 0
        return sum(self.orbits(e.to) + 1 for e in self.graph.edges[object])

    def orbit_chain(self, object: str) -> list[str]:
        if object == self.ROOT:
            return [object]
        orbits = self.graph.edges[object][0].to
        return [object] + self.orbit_chain(orbits)
