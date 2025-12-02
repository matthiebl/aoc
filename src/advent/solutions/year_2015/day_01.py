"""
--- Day 1: Not Quite Lisp ---
https://adventofcode.com/2015/day/1
"""

from advent.core import Solver


class Day01(Solver):
    """Solution for day 1."""

    def prepare(self):
        floors = [0]
        for move in self.input:
            floors.append(floors[-1] + (1 if move == "(" else -1))
        self.store.floors = floors

    def part1(self) -> int:
        """Solve part 1."""
        return self.store.floors[-1]

    def part2(self) -> int:
        """Solve part 2."""
        return self.store.floors.index(-1)
