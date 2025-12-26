import pytest

from advent.solutions.year_2025.day_01 import Day01
from advent.utils.input_string import InputString


@pytest.mark.parametrize("input, expected", [("L10", 0)])
def test_part1(input, expected):
    solver = get_solver(input)

    result = solver.part1()

    assert result == expected


def test_part2():
    solver = get_solver("L10\nR99")
    result = solver.part2()
    assert result == 1


def get_solver(input: str) -> Day01:
    solver = Day01(2025, 1)
    solver.input = InputString(input)
    solver.prepare()
    return solver
