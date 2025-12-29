"""
--- Day 3: Crossed Wires ---
https://adventofcode.com/2019/day/3
"""

from advent.core import Solver


class Day03(Solver):
    """Solution for day 3."""

    def prepare(self) -> None:
        self.store.points = []
        for line in self.input.lines():
            line_points = set()
            x, y = 0, 0
            for move in line.split(","):
                d = self.Point.direction_from(move[0])
                for _ in range(int(move[1:])):
                    x, y = x + d.x, y + d.y
                    line_points.add((x, y))
            self.store.points.append(line_points)

        assert len(self.store.points) == 2
        self.store.intersections = self.store.points[0] & self.store.points[1]

    def part1(self) -> int:
        """Solve part 1."""
        return min(abs(x) + abs(y) for x, y in self.store.intersections)

    def part2(self) -> int:
        """Solve part 2."""
        intersections = {p: [] for p in self.store.intersections}
        for line in self.input.lines():
            dist = 0
            x, y = 0, 0
            for move in line.split(","):
                d = self.Point.direction_from(move[0])
                for _ in range(int(move[1:])):
                    x, y = x + d.x, y + d.y
                    dist += 1
                    if (x, y) in intersections:
                        intersections[(x, y)].append(dist)

        return min(x + y for x, y in intersections.values())
