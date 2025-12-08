"""
--- Day 4: Printing Department ---
https://adventofcode.com/2025/day/4
"""

from advent.core import Solver


class Day04(Solver):
    """Solution for day 4."""
    PAPER = "@"
    EMPTY = "."

    def prepare(self):
        pass

    def part1(self) -> int:
        """Solve part 1."""
        grid = self.input.grid()
        removable = 0
        for p in grid.find_all(self.PAPER):
            rolls = sum(grid.get(pp) == self.PAPER
                        for pp in grid.neighbors8(p))
            if rolls < 4:
                removable += 1
        return removable

    def part2(self) -> int:
        """Solve part 2."""
        grid = self.input.grid()
        removed = 0
        while True:
            removable = []
            for p in grid.find_all(self.PAPER):
                rolls = sum(grid.get(pp) == self.PAPER
                            for pp in grid.neighbors8(p))
                if rolls < 4:
                    removable.append(p)
            if len(removable) == 0:
                break
            removed += len(removable)
            for p in removable:
                grid.set(p, self.EMPTY)
        return removed
