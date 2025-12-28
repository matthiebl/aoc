"""
--- Day 12: JSAbacusFramework.io ---
https://adventofcode.com/2015/day/12
"""

from json import loads

from advent.core import Solver


class Day12(Solver):
    """Solution for day 12."""

    def prepare(self):
        pass

    def part1(self) -> int:
        """Solve part 1."""
        return sum(self.input.nums())

    def part2(self) -> int:
        """Solve part 2."""
        return self.non_red_sum(loads(self.input))

    def non_red_sum(self, json) -> int:
        if isinstance(json, int):
            return json
        if isinstance(json, str):
            return 0
        if isinstance(json, list):
            return sum(self.non_red_sum(it) for it in json)
        assert isinstance(json, dict)
        if any(v == "red" for v in json.values()):
            return 0
        return sum(self.non_red_sum(v) for v in json.values())
