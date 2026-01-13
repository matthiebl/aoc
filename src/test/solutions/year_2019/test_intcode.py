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
def test_add(program: list[int], index: int, outcome: int) -> None:
    code = Intcode(program)
    code.run()
    assert code.memory[index] == outcome


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
def test_mul(program: list[int], index: int, outcome: int) -> None:
    code = Intcode(program)
    code.run()
    assert code.memory[index] == outcome


def test_boost_example_1():
    program = [109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99]
    code = Intcode(program)
    code.run()
    assert list(code.output) == program


def test_boost_example_2():
    program = [1102, 34915192, 34915192, 7, 4, 7, 99, 0]
    code = Intcode(program)
    code.run()
    assert code.output.pop() == 1219070632396864


def test_boost_example_3():
    program = [104, 1125899906842624, 99]
    code = Intcode(program)
    code.run()
    assert code.output.pop() == 1125899906842624
