"""Base solver class for Advent of Code problems."""

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any

from advent.utils import Utils
from advent.utils.grid import Grid
from advent.utils.input_string import InputString
from advent.utils.point import Point


class Store:
    """Simple storage class for arbitrary attributes."""

    pass


class Solver(ABC):
    """Base class for all AoC solution implementations."""

    def __init__(self, year: int, day: int) -> None:
        self.year: int = year
        self.day: int = day
        self.utils: Utils = Utils
        self.input: InputString = InputString("")
        self.Grid: Grid = Grid
        self.Point: Point = Point
        self.store: Store = Store()

    def load_input(self, input_path: str | None = None) -> None:
        """Load input data from file."""
        if input_path is None:
            input_path = Path(f"inputs/{self.year}/day_{self.day:02d}.txt")
        else:
            input_path = Path(input_path)

        if input_path.exists():
            data = input_path.read_text().strip()
            self.input = InputString(data)
        else:
            raise FileNotFoundError(f"Input file not found: {input_path}")

    @abstractmethod
    def prepare(self):
        pass

    @abstractmethod
    def part1(self) -> Any:
        """Solve part 1 of the problem."""
        pass

    @abstractmethod
    def part2(self) -> Any:
        """Solve part 2 of the problem."""
        pass

    def solve(self) -> tuple[Any, Any]:
        """Solve both parts and return results."""
        self.prepare()
        return self.part1(), self.part2()
