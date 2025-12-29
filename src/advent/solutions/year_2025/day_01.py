"""
--- Day 1: Secret Entrance ---
https://adventofcode.com/2025/day/1
"""

from advent.core import Solver


class Day01(Solver):
    """Solution for day 1."""

    DIAL_START = 50
    DIAL_SIZE = 100

    def prepare(self) -> None:
        direction = {"L": -1, "R": 1}
        self.store.rotations = [
            direction[instruction[0]] * int(instruction[1:]) for instruction in self.input.lines()
        ]

    def part1(self) -> int:
        """Solve part 1."""
        at_zero = 0
        dial = self.DIAL_START
        for rotation in self.store.rotations:
            dial = (dial + rotation) % self.DIAL_SIZE
            if dial == 0:
                at_zero += 1
        return at_zero

    def part2(self) -> int:
        """Solve part 2."""
        passed_zero = 0
        dial = self.DIAL_START
        for rotation in self.store.rotations:
            passed_zero += abs(rotation) // self.DIAL_SIZE
            before = dial
            dial = (dial + rotation) % self.DIAL_SIZE
            if before != 0 and (
                dial == 0 or rotation < 0 and (dial >= before) or rotation > 0 and dial <= before
            ):
                passed_zero += 1
        return passed_zero
