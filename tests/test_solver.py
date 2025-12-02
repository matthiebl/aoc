"""Tests for the base Solver class."""

from pathlib import Path
from advent.core import Solver


class ExampleSolver(Solver):
    """Test implementation of Solver."""

    def part1(self) -> int:
        return len(self.input.lines())

    def part2(self) -> int:
        return len(self.input)


def test_solver_basic(tmp_path: Path) -> None:
    """Test basic solver functionality."""
    # Create test input
    input_file = tmp_path / "test_input.txt"
    input_file.write_text("line1\nline2\nline3")

    solver = ExampleSolver(2024, 1)
    solver.load_input(input_file)

    assert solver.part1() == 3
    assert solver.part2() == 17
