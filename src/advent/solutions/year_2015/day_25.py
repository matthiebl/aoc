"""
--- Day 25: Let It Snow ---
https://adventofcode.com/2015/day/25
"""

from advent.core import Solver


class Day25(Solver):
    """Solution for day 25."""

    def prepare(self) -> None:
        pass

    def part1(self) -> int:
        """Solve part 1."""
        rows, cols = self.input.nums()
        code = 20151125
        r, c = 2, 1
        while (r, c) != (rows, cols):
            code = (code * 252533) % 33554393
            if r == 1:
                r = c + 1
                c = 1
            else:
                r -= 1
                c += 1
        return (code * 252533) % 33554393

    def part2(self) -> None:
        """Solve part 2."""
        return None
