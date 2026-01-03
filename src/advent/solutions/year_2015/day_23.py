"""
--- Day 23: Opening the Turing Lock ---
https://adventofcode.com/2015/day/23
"""

from advent.core import Solver
from advent.utils.input_string import InputString
from advent.utils.interpreter import Interpreter


class Day23(Solver):
    """Solution for day 23."""

    def prepare(self) -> None:
        pass

    def part1(self) -> int:
        """Solve part 1."""
        interpreter = self.TuringLock().parse_instructions(self.input)
        return interpreter.run().value("b")

    def part2(self) -> int:
        """Solve part 2."""
        interpreter = self.TuringLock(a=1).parse_instructions(self.input)
        return interpreter.run().value("b")

    class TuringLock(Interpreter):
        def parse_instructions(self, raw: InputString) -> "Day23.TuringLock":
            for line in raw.lines():
                [op, *args] = line.split()
                if op in ["jie", "jio"]:
                    self.instructions.append([op, args[0][:-1], args[1]])
                else:
                    self.instructions.append([op, *args])
            self.length = len(self.instructions)
            return self

        def _op_jie(self, x: str, y: str) -> int:
            return self.value(y) if self.value(x) % 2 == 0 else 1

        def _op_jio(self, x: str, y: str) -> int:
            return self.value(y) if self.value(x) == 1 else 1
