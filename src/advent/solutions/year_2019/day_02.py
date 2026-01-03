"""
--- Day 2: 1202 Program Alarm ---
https://adventofcode.com/2019/day/2
"""

from advent.core import Solver
from advent.solutions.year_2019.intcode import Intcode


class Day02(Solver):
    """Solution for day 2."""

    TARGET = 19690720

    def prepare(self) -> None:
        pass

    def part1(self) -> int:
        """Solve part 1."""
        code = Intcode(list(self.input.nums()), replace={1: 12, 2: 2})
        code.run()
        return code.memory[0]

    def part2(self) -> int:
        """Solve part 2."""
        program = list(self.input.nums())
        for noun in range(100):
            for verb in range(100):
                code = Intcode(program.copy(), replace={1: noun, 2: verb})
                code.run()
                if code.memory[0] == self.TARGET:
                    return 100 * noun + verb
        return 0
