"""Input string utilities with parsing methods."""

from re import findall
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from advent.utils.grid import Grid


class InputString(str):
    """Parsing utilities for common input patterns."""

    def nums(self, string: str | None = None) -> list[int]:
        """Returns all numbers in the object, otherwise the provided string"""
        string = self if string is None else string
        return list(map(int, findall(r"(-?\d+)", string)))

    def lines(self, string: str | None = None) -> list["InputString"]:
        """Returns the lines in the object, otherwise the provided string"""
        string = self if string is None else string
        return list(map(InputString, string.strip().split("\n")))

    def sections(self, string: str | None = None) -> list["InputString"]:
        """Returns the lines in the object, otherwise the provided string"""
        string = self if string is None else string
        return list(map(InputString, string.strip().split("\n\n")))

    def grid(self) -> "Grid":
        """Parse text into a 2D grid of characters."""
        # Import here to avoid circular import
        from advent.utils.grid import Grid

        return Grid.from_string(self)

    def num_grid(self) -> "Grid":
        """Parse text into a 2D grid of ints."""
        # Import here to avoid circular import
        from advent.utils.grid import Grid

        return Grid.from_num_string(self)
