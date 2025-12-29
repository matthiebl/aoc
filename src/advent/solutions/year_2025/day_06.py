"""
--- Day 6: Trash Compactor ---
https://adventofcode.com/2025/day/6
"""

from functools import reduce

from advent.core import Solver


class Day06(Solver):
    """Solution for day 6."""

    def prepare(self) -> None:
        self.store.operations = self.input.lines()[-1].replace(" ", "")

    def part1(self) -> int:
        """Solve part 1."""
        problems = list(
            zip(self.store.operations, zip(*[line.nums() for line in self.input.lines()[:-1]]))
        )
        return sum(self.cephalopod_math(operation, ns) for operation, ns in problems)

    def part2(self) -> int:
        """Solve part 2."""
        lines = self.input.lines()[:-1]
        numbers = "_".join(map(lambda x: "".join(x).replace(" ", ""), zip(*lines))).split("__")
        problems = list(
            zip(self.store.operations, map(lambda x: tuple(self.input.nums(x)), numbers))
        )
        return sum(self.cephalopod_math(operation, ns) for operation, ns in problems)

    def cephalopod_math(self, operation: str, ns: tuple[int, ...]) -> int:
        if operation == "*":
            return reduce(lambda x, y: x * y, ns)
        return sum(ns)
