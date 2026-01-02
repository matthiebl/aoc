"""
--- Day 20: Infinite Elves and Infinite Houses ---
https://adventofcode.com/2015/day/20
"""

import numpy as np

from advent.core import Solver


class Day20(Solver):
    """Solution for day 20."""

    def prepare(self) -> None:
        self.presents = self.input.nums()[0]

    def part1(self) -> int:
        """Solve part 1."""
        houses = np.full(self.presents // 10, 10, dtype=int)
        for elf in range(2, self.presents // 10):
            houses[elf::elf] += elf * 10
        return int(np.argmax(houses >= self.presents))

    def part2(self) -> int:
        """Solve part 2."""
        houses = np.full(self.presents // 10, 10, dtype=int)
        for elf in range(2, self.presents // 10):
            houses[elf : 50 * elf + 1 : elf] += elf * 11
        return int(np.argmax(houses >= self.presents))
