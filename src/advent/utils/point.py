"""Point and coordinate utilities."""

from collections.abc import Iterator
from dataclasses import dataclass
from typing import ClassVar


@dataclass(frozen=True)
class Point:
    """2D point with common operations."""

    x: int
    y: int

    # Direction constants (defined after class)
    NORTH: ClassVar["Point"]
    SOUTH: ClassVar["Point"]
    EAST: ClassVar["Point"]
    WEST: ClassVar["Point"]
    NORTH_EAST: ClassVar["Point"]
    SOUTH_EAST: ClassVar["Point"]
    SOUTH_WEST: ClassVar["Point"]
    NORTH_WEST: ClassVar["Point"]
    CLOCK_4: ClassVar[list["Point"]]
    CLOCK_8: ClassVar[list["Point"]]

    def __add__(self, other: "Point") -> "Point":
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Point") -> "Point":
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: int) -> "Point":
        return Point(self.x * scalar, self.y * scalar)

    def distance(self, other: "Point") -> float:
        """Calculate Euclidean distance to another point."""
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def manhattan_distance(self, other: "Point") -> int:
        """Calculate Manhattan distance to another point."""
        return abs(self.x - other.x) + abs(self.y - other.y)

    def neighbors4(self) -> Iterator["Point"]:
        """Yield 4 orthogonal neighbors (up, down, left, right)."""
        yield Point(self.x, self.y - 1)  # up
        yield Point(self.x + 1, self.y)  # right
        yield Point(self.x, self.y + 1)  # down
        yield Point(self.x - 1, self.y)  # left

    def neighbors8(self) -> Iterator["Point"]:
        """Yield 8 neighbors including diagonals."""
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                yield Point(self.x + dx, self.y + dy)


# Define direction constants after the class is fully defined
Point.NORTH = Point(0, -1)
Point.SOUTH = Point(0, 1)
Point.EAST = Point(1, 0)
Point.WEST = Point(-1, 0)
Point.NORTH_EAST = Point(1, -1)
Point.SOUTH_EAST = Point(-1, 1)
Point.SOUTH_WEST = Point(-1, 1)
Point.NORTH_WEST = Point(1, -1)
Point.CLOCK_4 = [Point.NORTH, Point.EAST, Point.SOUTH, Point.WEST]
Point.CLOCK_8 = [
    Point.NORTH,
    Point.NORTH_EAST,
    Point.EAST,
    Point.SOUTH_EAST,
    Point.SOUTH,
    Point.SOUTH_WEST,
    Point.WEST,
    Point.NORTH_WEST,
]
