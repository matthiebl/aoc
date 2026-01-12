"""
--- Day 7: Amplification Circuit ---
https://adventofcode.com/2019/day/7
"""

from collections import deque
from itertools import permutations
from typing import Any

from advent.core import Solver
from advent.solutions.year_2019.intcode import Intcode


class PausingIntcode(Intcode):
    """
    This version of Intcode simply pauses the program after the output instruction,
    which allows the input cycle not to break.
    """

    def running(self) -> bool:
        return super().running() and not self.paused

    def run(self) -> None:
        self.paused = False
        return super().run()

    def _op_output(self, modes: list[int], **kwargs: Any) -> None:
        self.paused = True
        return super()._op_output(modes, **kwargs)


class Day07(Solver):
    """Solution for day 7."""

    AMPLIFIERS = 5

    def prepare(self) -> None:
        self.program = self.input.nums()

    def part1(self) -> int:
        """Solve part 1."""
        return self.max_thrust(range(self.AMPLIFIERS))

    def part2(self) -> int:
        """Solve part 2."""
        return self.max_thrust(range(self.AMPLIFIERS, 2 * self.AMPLIFIERS))

    def max_thrust(self, phase_range: range) -> int:
        """
        Cycle through amplifier programs until an amplifier officially halts.
        The last amplifier will get queued an extra input, which we use to get the thrust value.
        """
        max_thrust = 0
        for phases in permutations(phase_range):
            amplifiers = deque([PausingIntcode(self.program, queue=[n]) for n in phases])
            inputs = deque([0])
            while True:
                amplifier = amplifiers.popleft()
                amplifier.input.append(inputs.popleft())
                amplifier.run()
                if amplifier.halted:
                    break
                inputs.append(amplifier.output.pop())
                amplifiers.append(amplifier)
            max_thrust = max(max_thrust, amplifier.input.pop())
        return max_thrust
