"""
--- Day 5: Cafeteria ---
https://adventofcode.com/2025/day/5
"""

from advent.core import Solver


class Day05(Solver):
    """Solution for day 5."""

    def prepare(self):
        ranges, items = self.input.sections()
        self.store.ranges = sorted(self.utils.chunks(map(abs, ranges.nums())), reverse=True)
        self.store.items = list(items.nums())

    def is_fresh(self, item: int):
        return any(l <= item <= r for l, r in self.store.ranges)

    def part1(self) -> int:
        """Solve part 1."""
        return sum(self.is_fresh(item) for item in self.store.items)

    def part2(self) -> int:
        """Solve part 2."""
        total = 0
        pl, pr = self.store.ranges.pop()
        while self.store.ranges:
            cl, cr = self.store.ranges.pop()
            if pr <= cl:
                total += pr - pl + (0 if pr == cl else 1)
                pl, pr = cl, cr
            else:
                pl, pr = min(pl, cl), max(pr, cr)
        return total + pr + 1 - pl
