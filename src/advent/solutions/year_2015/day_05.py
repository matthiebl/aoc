"""
--- Day 5: Doesn't He Have Intern-Elves For This? ---
https://adventofcode.com/2015/day/5
"""

import re

from advent.core import Solver


class Day05(Solver):
    """Solution for day 5."""

    def prepare(self) -> None:
        pass

    def part1(self) -> int:
        """Solve part 1."""

        def nice(string: str) -> bool:
            if re.search(r"ab|cd|pq|xy", string):
                return False
            return (
                any(a == b for a, b in self.utils.windows(string))
                and len(re.findall(r"a|e|i|o|u", string)) >= 3
            )

        return len(list(filter(nice, self.input.lines())))

    def part2(self) -> int:
        """Solve part 2."""

        def nice(string: str) -> bool:
            return any(string.count(a + b) >= 2 for a, b in self.utils.windows(string)) and any(
                a == b for a, b in zip(string, string[2:])
            )

        return len(list(filter(nice, self.input.lines())))
