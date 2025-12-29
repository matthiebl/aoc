"""
--- Day 2: I Was Told There Would Be No Math ---
https://adventofcode.com/2015/day/2
"""

from advent.core import Solver


class Day02(Solver):
    """Solution for day 2."""

    def prepare(self) -> None:
        self.store.presents = list(map(sorted, self.utils.chunks(self.input.nums(), n=3)))

    def part1(self) -> int:
        """Solve part 1."""
        return sum(3 * w * h + 2 * (w * d + h * d) for w, h, d in self.store.presents)

    def part2(self) -> int:
        """Solve part 2."""
        return sum(2 * (w + h) + w * h * d for w, h, d in self.store.presents)
