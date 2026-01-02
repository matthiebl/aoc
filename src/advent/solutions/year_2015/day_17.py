"""
--- Day 17: No Such Thing as Too Much ---
https://adventofcode.com/2015/day/17
"""

from collections import defaultdict

from advent.core import Solver


class Day17(Solver):
    """Solution for day 17."""

    def prepare(self) -> None:
        self.containers = self.input.nums()
        self.size: dict[int, int] = defaultdict(int)

    def part1(self) -> int:
        """Solve part 1."""
        return self.container_combinations()

    def part2(self) -> int:
        """Solve part 2."""
        minimum_containers: int = self.size[sorted(self.size)[0]]
        return minimum_containers

    def container_combinations(
        self, total: int = 0, target: int = 150, taken: int = 0, i: int = 0
    ) -> int:
        if i == len(self.containers):
            if total == target:
                self.size[taken] += 1
                return 1
            return 0
        return self.container_combinations(
            total + self.containers[i], target, taken + 1, i + 1
        ) + self.container_combinations(total, target, taken, i + 1)
