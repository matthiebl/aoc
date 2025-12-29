"""
--- Day 10: Elves Look, Elves Say ---
https://adventofcode.com/2015/day/10
"""

from advent.core import Solver


class Day10(Solver):
    """Solution for day 10."""

    def prepare(self) -> None:
        pass

    def part1(self) -> int:
        """Solve part 1."""
        code = self.input
        for _ in range(40):
            code = self.look_and_say(code)
        return len(code)

    def part2(self) -> int:
        """Solve part 2."""
        code = self.input
        for _ in range(50):
            code = self.look_and_say(code)
        return len(code)

    def look_and_say(self, code: str) -> str:
        said, cur, length = "", code[0], 1
        for nxt in code[1:]:
            if nxt == cur:
                length += 1
            else:
                said += f"{length}{cur}"
                cur, length = nxt, 1
        said += f"{length}{cur}"
        return said
