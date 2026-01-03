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


@pytest.mark.parametrize(
    "opcode, exp_code, exp_modes",
    [
        (1, 1, [0, 0, 0]),
        (101, 1, [1, 0, 0]),
        (1001, 1, [0, 1, 0]),
        (11101, 1, [1, 1, 1]),
    ],
)
def test_get_opcode(opcode, exp_code, exp_modes):
    code = Intcode([opcode])
    act_code, act_modes = code.get_opcode()
    assert exp_code == act_code
    assert exp_modes == act_modes[: len(exp_modes)]
