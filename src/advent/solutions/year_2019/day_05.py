"""
--- Day 5: Sunny with a Chance of Asteroids ---
https://adventofcode.com/2019/day/5
"""

from advent.core import Solver
from advent.solutions.year_2019.intcode import Intcode


class Day05(Solver):
    """Solution for day 5."""

    def prepare(self) -> None:
        pass

    def part1(self) -> int:
        """Solve part 1."""
        code = Intcode(self.input.nums())
        code.add_input(1)
        code.run()
        diagnostic: int = code.output[-1]
        return diagnostic

    def part2(self) -> int:
        """Solve part 2."""
        code = Intcode(self.input.nums())
        code.add_input(5)
        code.run()
        diagnostic: int = code.output[-1]
        return diagnostic
