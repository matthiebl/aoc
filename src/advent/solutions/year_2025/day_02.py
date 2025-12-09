"""
--- Day 2: Gift Shop ---
https://adventofcode.com/2025/day/2
"""

from advent.core import Solver


class Day02(Solver):
    """Solution for day 2."""

    def prepare(self):
        self.store.ranges = list(
            map(lambda x: tuple(map(int, x.split("-"))), self.input.split(","))
        )

    def part1(self) -> int:
        """Solve part 1."""
        invalid_sum = 0
        for a, b in self.store.ranges:
            for n in range(a, b + 1):
                id_ = str(n)
                length = len(id_)
                if length % 2 == 0 and id_[: length // 2] == id_[length // 2 :]:
                    invalid_sum += n
        return invalid_sum

    def part2(self) -> int:
        """Solve part 2."""
        invalid_sum = 0
        for a, b in self.store.ranges:
            for n in range(a, b + 1):
                id_ = str(n)
                length = len(id_)
                for l in range(1, length // 2 + 1):
                    if id_ == (id_[:l] * (length // l)):
                        invalid_sum += n
                        break
        return invalid_sum
