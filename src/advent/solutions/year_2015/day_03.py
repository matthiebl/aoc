"""
--- Day 3: Perfectly Spherical Houses in a Vacuum ---
https://adventofcode.com/2015/day/3
"""

from advent.core import Solver


class Day03(Solver):
    """Solution for day 3."""

    def prepare(self):
        pass

    def part1(self) -> int:
        """Solve part 1."""
        p = self.Point.of(0, 0)
        gifted = set([p])
        for move in self.input:
            p += self.Point.direction_from(move)
            gifted.add(p)
        return len(gifted)

    def part2(self) -> int:
        """Solve part 2."""
        p1 = self.Point.of(0, 0)
        p2 = self.Point.of(0, 0)
        gifted = set([p1, p2])
        for move1, move2 in self.utils.chunks(self.input):
            p1 += self.Point.direction_from(move1)
            p2 += self.Point.direction_from(move2)
            gifted |= set([p1, p2])
        return len(gifted)
