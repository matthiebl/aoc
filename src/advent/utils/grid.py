"""Grid utilities for 2D problems."""

from collections.abc import Iterator
from typing import TYPE_CHECKING

from advent.utils.point import Point

if TYPE_CHECKING:
    from advent.utils.input_string import InputString


class Grid[T]:
    """2D grid with common operations."""

    def __init__(self, data: list[list[T]]) -> None:
        self.data = data
        self.height = len(data)
        self.width = len(data[0]) if data else 0

    @classmethod
    def from_string(cls, text: "InputString") -> "Grid":
        """Create a grid from a string (one line per row)."""
        return cls([list(map(str, line)) for line in text.lines()])  # type: ignore

    @classmethod
    def from_num_string(cls, text: "InputString") -> "Grid":
        """Create a grid from a string (one line per row), where each character is a number."""
        return cls([list(map(int, line)) for line in text.lines()])  # type: ignore

    def get(self, point: Point, default: T | None = None) -> T | None:
        """Get value at point, or default if out of bounds."""
        if not self.in_bounds(point):
            return default
        return self.data[point.y][point.x]

    def set(self, point: Point, value: T) -> None:
        """Set value at point."""
        if self.in_bounds(point):
            self.data[point.y][point.x] = value

    def in_bounds(self, point: Point) -> bool:
        """Check if point is within grid bounds."""
        return 0 <= point.x < self.width and 0 <= point.y < self.height

    def find(self, value: T) -> Point:
        """Find first occurrence of value in grid."""
        for point in self.all_points():
            if self.get(point) == value:
                return point
        raise KeyError(f"Value `{value}` does not exist in the grid")

    def find_all(self, value: T) -> list[Point]:
        """Find all occurrences of value in grid."""
        return [point for point in self.all_points() if self.get(point) == value]

    def all_points(self) -> Iterator[Point]:
        """Iterate over all points in the grid."""
        for y in range(self.height):
            for x in range(self.width):
                yield Point(x, y)

    def neighbors4(self, point: Point) -> Iterator[Point]:
        """Yield valid 4-directional neighbors."""
        for neighbor in point.neighbors4():
            if self.in_bounds(neighbor):
                yield neighbor

    def neighbors8(self, point: Point) -> Iterator[Point]:
        """Yield valid 8-directional neighbors."""
        for neighbor in point.neighbors8():
            if self.in_bounds(neighbor):
                yield neighbor

    def __iter__(self) -> Iterator[tuple[Point, T]]:
        """Iterate over all (point, value) pairs in the grid."""
        for point in self.all_points():
            yield point, self.data[point.y][point.x]

    def __str__(self) -> str:
        """String representation of the grid."""
        return "\n".join("".join(str(cell) for cell in row) for row in self.data)
