"""
--- Day 4: The Ideal Stocking Stuffer ---
https://adventofcode.com/2015/day/4
"""

from _md5 import md5

from advent.core import Solver


class Day04(Solver):
    """Solution for day 4."""

    def prepare(self):
        pass

    def part1(self) -> int:
        """Solve part 1."""
        i = 0
        while True:
            hash = md5(f"{self.input}{i}".encode()).hexdigest()
            if hash.startswith("00000"):
                return i
            i += 1

    def part2(self) -> int:
        """Solve part 2."""
        i = 0
        while True:
            hash = md5(f"{self.input}{i}".encode()).hexdigest()
            if hash.startswith("000000"):
                return i
            i += 1
