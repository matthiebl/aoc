"""
--- Day 7: Some Assembly Required ---
https://adventofcode.com/2015/day/7
"""

from functools import cache
from re import search

from advent.core import Solver


class Day07(Solver):
    """Solution for day 7."""

    def prepare(self):
        self.store.wires = {k: v for v, k in [line.split(" -> ") for line in self.input.lines()]}

    def part1(self) -> int:
        """Solve part 1."""
        self.compute.cache_clear()
        return self.compute("a")

    def part2(self) -> int:
        """Solve part 2."""
        self.store.wires["b"] = str(self.part1())
        self.compute.cache_clear()
        return self.compute("a")

    @cache
    def compute(self, wire: str) -> int:
        if wire.isnumeric():
            return int(wire)
        gate = self.store.wires[wire]
        if gate.isnumeric():
            return int(gate)
        if len(gate) <= 2:
            return self.compute(gate)
        if gate.startswith("NOT"):
            return (2**17 - 1) ^ self.compute(gate[4:])
        x, op, y = search(r"(\w+) (\w+) (\w+)", gate).groups()
        if op == "OR":
            return self.compute(x) | self.compute(y)
        if op == "AND":
            return self.compute(x) & self.compute(y)
        if op == "LSHIFT":
            return self.compute(x) << self.compute(y)
        if op == "RSHIFT":
            return self.compute(x) >> self.compute(y)
