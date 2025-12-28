"""
--- Day 8: Matchsticks ---
https://adventofcode.com/2015/day/8
"""

from advent.core import Solver


class Day08(Solver):
    """Solution for day 8."""

    def prepare(self):
        pass

    def part1(self) -> int:
        """Solve part 1."""
        return sum(
            len(s) - len(s.encode().decode("unicode-escape")) + 2 for s in self.input.lines()
        )

    def part2(self) -> int:
        """Solve part 2."""
        return sum(len(repr(s)) - len(s) + s.count('"') for s in self.input.lines())
