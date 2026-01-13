"""
--- Day 8: Space Image Format ---
https://adventofcode.com/2019/day/8
"""

from advent.core import Solver
from advent.utils.input_string import InputString


class Day08(Solver):
    """Solution for day 8."""

    WIDTH = 25
    HEIGHT = 6

    TRANSPARENT = "2"

    def prepare(self) -> None:
        layer_size = self.WIDTH * self.HEIGHT
        self.layers = ["".join(layer) for layer in self.utils.chunks(self.input, n=layer_size)]

    def part1(self) -> int:
        """Solve part 1."""
        zeros = [layer.count("0") for layer in self.layers]
        counts = [layer.count("1") * layer.count("2") for layer in self.layers]
        _, count = next(iter(sorted(zip(zeros, counts))))
        return count

    def part2(self) -> str:
        """Solve part 2."""
        image = self.layers[-1]
        for layer in self.layers[::-1]:
            image = "".join(b if b != self.TRANSPARENT else a for a, b in zip(image, layer))
        return image
