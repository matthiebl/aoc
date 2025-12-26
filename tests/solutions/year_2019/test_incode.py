import pytest

from advent.solutions.year_2019.intcode import Intcode


@pytest.mark.parametrize(
    "program, index, outcome",
    [
        ([1, 1, 2, 0, 99], 0, 3),
        ([1, 2, 2, 0, 99], 0, 4),
        ([1, 2, 3, 3, 99], 3, 6),
        ([1, 5, 6, 4, 0, 50, 49], 4, 99),
    ],
)
def test_add(program, index, outcome):
    code = Intcode(program)
    code.run()
    assert code.get(index) == outcome


@pytest.mark.parametrize(
    "program, index, outcome",
    [
        ([2, 1, 2, 0, 99], 0, 2),
        ([2, 2, 3, 0, 99], 0, 0),
        ([2, 4, 0, 0, 99], 0, 198),
        ([2, 2, 3, 3, 99], 3, 9),
        ([2, 5, 6, 4, 0, 3, 33], 4, 99),
    ],
)
def test_mul(program, index, outcome):
    code = Intcode(program)
    code.run()
    assert code.get(index) == outcome
