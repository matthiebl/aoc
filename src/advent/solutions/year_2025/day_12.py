"""
--- Day 12: Christmas Tree Farm ---
https://adventofcode.com/2025/day/12
"""

from advent.core import Solver


class Day12(Solver):
    """Solution for day 12."""

    def prepare(self) -> None:
        [*presents, orders] = self.input.sections()
        self.store.present_size = [p.count("#") for p in presents]
        self.store.orders = [list(self.input.nums(order)) for order in orders.lines()]

    def part1(self) -> int:
        """Solve part 1."""
        fit = 0
        for order in self.store.orders:
            [w, h, *n_shapes] = order
            area = w * h
            used = sum(size * n for size, n in zip(self.store.present_size, n_shapes))
            if used <= area:
                fit += 1
        return fit

    def part2(self) -> None:
        """No part 2 for final day!"""
        return None
