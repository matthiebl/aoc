"""
--- Day 1: The Tyranny of the Rocket Equation ---
https://adventofcode.com/2019/day/1
"""

from advent.core import Solver


class Day01(Solver):
    """Solution for day 1."""

    def prepare(self):
        pass

    def part1(self) -> int:
        """Solve part 1."""
        return sum(self.fuel(n) for n in self.input.nums())

    def part2(self) -> int:
        """Solve part 2."""
        return sum(self.fuel(n, recursive=True) for n in self.input.nums())

    def fuel(self, mass: int, recursive: bool = False) -> int:
        fuel = mass // 3 - 2
        if fuel <= 0:
            return 0
        if recursive:
            return fuel + self.fuel(fuel, recursive)
        return fuel
