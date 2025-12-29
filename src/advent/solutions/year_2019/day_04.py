"""
--- Day 4: Secure Container ---
https://adventofcode.com/2019/day/4
"""

from advent.core import Solver


class Day04(Solver):
    """Solution for day 4."""

    def prepare(self) -> None:
        pass

    def part1(self) -> int:
        """Solve part 1."""
        low, high = list(map(int, self.input.split("-")))
        valid = 0
        for n in range(low, high + 1):
            if self.is_non_decreasing(n) and self.has_adjacent(n):
                valid += 1
        return valid

    def part2(self) -> int:
        """Solve part 2."""
        low, high = list(map(int, self.input.split("-")))
        valid = 0
        for n in range(low, high + 1):
            if self.is_non_decreasing(n) and self.has_single_adjacent(n):
                valid += 1
        return valid

    def is_non_decreasing(self, n: int) -> bool:
        return all(a <= b for a, b in self.utils.windows(str(n)))

    def has_adjacent(self, n: int) -> bool:
        return any(a == b for a, b in self.utils.windows(str(n)))

    def has_single_adjacent(self, n: int) -> bool:
        n = str(n)
        last = n[0]
        length = 0
        for x in n:
            if x == last:
                length += 1
            elif length == 2:
                return True
            else:
                last = x
                length = 1
        return length == 2
