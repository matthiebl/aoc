"""
--- Day 18: Like a GIF For Your Yard ---
https://adventofcode.com/2015/day/18
"""

from advent.core import Solver
from advent.utils.grid import Grid
from advent.utils.point import Point


class Day18(Solver):
    """Solution for day 18."""

    ON = "#"
    OFF = "."

    def prepare(self) -> None:
        pass

    def part1(self) -> int:
        """Solve part 1."""
        grid = self.input.grid()
        self.step(grid, 100)
        return len(grid.find_all(self.ON))

    def part2(self) -> int:
        """Solve part 2."""
        grid = self.input.grid()
        always_on = [
            self.Point.of(0, 0),
            self.Point.of(0, grid.height - 1),
            self.Point.of(grid.width - 1, 0),
            self.Point.of(grid.width - 1, grid.height - 1),
        ]
        for p in always_on:
            grid.set(p, self.ON)
        self.step(grid, 100, always_on)
        return len(grid.find_all(self.ON))

    def step(self, grid: Grid, n: int = 1, permanent: list[Point] = []) -> None:
        for _ in range(n):
            turn_on: list[Point] = permanent.copy()
            for p, v in grid:
                on = sum(grid.get(np) == self.ON for np in grid.neighbors8(p))
                if v == self.ON and 2 <= on <= 3:
                    turn_on.append(p)
                elif v == self.OFF and on == 3:
                    turn_on.append(p)
            grid.set_all(self.OFF)
            for p in turn_on:
                grid.set(p, self.ON)
