"""
--- Day 3: Crossed Wires ---
https://adventofcode.com/2019/day/3
"""

from advent.core import Solver
from advent.utils.point import Point


class Day03(Solver):
    """Solution for day 3."""

    def prepare(self) -> None:
        self.store.points = []
        for line in self.input.lines():
            line_points = set()
            p = self.Point.of(0, 0)
            for move in line.split(","):
                d = self.Point.direction_from(move[0])
                for _ in range(int(move[1:])):
                    p += d
                    line_points.add(p)
            self.store.points.append(line_points)

        assert len(self.store.points) == 2
        self.store.intersections = self.store.points[0] & self.store.points[1]

    def part1(self) -> int:
        """Solve part 1."""
        closest_intersection: int = min(abs(p.x) + abs(p.y) for p in self.store.intersections)
        return closest_intersection

    def part2(self) -> int:
        """Solve part 2."""
        intersections: dict[Point, list[int]] = {p: [] for p in self.store.intersections}
        for line in self.input.lines():
            dist = 0
            p = self.Point.of(0, 0)
            for move in line.split(","):
                d = self.Point.direction_from(move[0])
                for _ in range(int(move[1:])):
                    p += d
                    dist += 1
                    if p in intersections:
                        intersections[p].append(dist)

        closest_intersection_by_walk: int = min(x + y for x, y in intersections.values())
        return closest_intersection_by_walk
