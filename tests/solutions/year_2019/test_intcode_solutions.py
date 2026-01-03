from advent.solutions.year_2019.day_02 import Day02


def test_day_2():
    solver = Day02(2019, 2)
    solver.load_input()
    part1, part2 = solver.solve()
    assert part1 == 5534943
    assert part2 == 7603
