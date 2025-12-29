"""
--- Day 6: Probably a Fire Hazard ---
https://adventofcode.com/2015/day/6
"""

import numpy as np

from advent.core import Solver


class Day06(Solver):
    """Solution for day 6."""

    def prepare(self) -> None:
        pass

    def part1(self) -> int:
        """Solve part 1."""
        lights = np.zeros((1000, 1000), dtype=int)
        for command in self.input.lines():
            r1, c1, r2, c2 = command.nums()
            sr, sc = slice(r1, r2 + 1), slice(c1, c2 + 1)
            match command[:7]:
                case "toggle ":
                    lights[sr, sc] ^= 1
                case "turn on":
                    lights[sr, sc] = 1
                case "turn of":
                    lights[sr, sc] = 0
        return sum(sum(lights))

    def part2(self) -> int:
        """Solve part 2."""
        brightness = np.zeros((1000, 1000), dtype=int)
        for command in self.input.lines():
            r1, c1, r2, c2 = command.nums()
            sr, sc = slice(r1, r2 + 1), slice(c1, c2 + 1)
            match command[:7]:
                case "toggle ":
                    brightness[sr, sc] += 2
                case "turn on":
                    brightness[sr, sc] += 1
                case "turn of":
                    brightness[sr, sc] -= 1
                    brightness[brightness < 0] = 0
        return sum(sum(brightness))
