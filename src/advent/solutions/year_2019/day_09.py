"""
--- Day 9: Sensor Boost ---
https://adventofcode.com/2019/day/9
"""

from advent.core import Solver
from advent.solutions.year_2019.intcode import Intcode


class Day09(Solver):
    """Solution for day 9."""

    def prepare(self) -> None:
        pass

    def part1(self) -> int:
        """Solve part 1."""
        boost = Intcode(self.input.nums(), queue=[1])
        boost.run()
        return boost.output.pop()

    def part2(self) -> int:
        """Solve part 2."""
        boost = Intcode(self.input.nums(), queue=[2])
        boost.run()
        return boost.output.pop()
