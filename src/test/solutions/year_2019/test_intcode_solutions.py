from advent.solutions.year_2019.day_02 import Day02
from advent.solutions.year_2019.day_05 import Day05


def test_day_2() -> None:
    solver = Day02(2019, 2)
    solver.load_input()
    part1, part2 = solver.solve()
    assert part1 == 5534943
    assert part2 == 7603


def test_day_5() -> None:
    solver = Day05(2019, 5)
    solver.load_input()
    part1, part2 = solver.solve()
    assert part1 == 8332629
    assert part2 == 8805067
