"""
--- Day 7: Laboratories ---
https://adventofcode.com/2025/day/7
"""

from functools import cache

from advent.core import Solver
from advent.utils.point import Point


class Day07(Solver):
    """Solution for day 7."""

    START = "S"
    EMPTY = "."
    SPLIT = "^"

    def prepare(self):
        pass

    def part1(self) -> int:
        """Solve part 1."""
        grid = self.input.grid()

        splitters = set()
        visited = set()
        search = [grid.find(self.START)]
        while search:
            p = search.pop()
            if (p.x, p.y) in splitters or (p.x, p.y) in visited:
                continue
            visited.add((p.x, p.y))
            while grid.in_bounds(p) and grid.get(p) != self.SPLIT:
                p += p.SOUTH
            if not grid.in_bounds(p):
                continue
            splitters.add((p.x, p.y))
            search.append(p + p.WEST)
            search.append(p + p.EAST)

        return len(splitters)

    def part2(self) -> int:
        """Solve part 2."""
        grid = self.input.grid()

        @cache
        def timelines(p: Point):
            while grid.in_bounds(p) and grid.get(p) != self.SPLIT:
                p += p.SOUTH
            if not grid.in_bounds(p):
                return 1
            return timelines(p + p.WEST) + timelines(p + p.EAST)

        return timelines(grid.find(self.START))
