"""
--- Day 15: Science for Hungry People ---
https://adventofcode.com/2015/day/15
"""

from collections.abc import Callable, Generator
from functools import reduce

from advent.core import Solver


class Day15(Solver):
    """Solution for day 15."""

    TEASPOONS = 100
    CALORIE_TARGET = 500

    def prepare(self) -> None:
        self.store.ingredients = list(self.utils.chunks(self.input.nums(), n=5))

    def part1(self) -> int:
        """Solve part 1."""
        return self.find_best_score_for(lambda prop: all(p > 0 for p in prop[:-1]))

    def part2(self) -> int:
        """Solve part 2."""
        return self.find_best_score_for(
            lambda prop: all(p > 0 for p in prop) and prop[-1] == self.CALORIE_TARGET
        )

    def find_best_score_for(self, predicate: Callable[[tuple[int, ...]], bool]) -> int:
        highest_score = 0
        for teaspoons in self.nums_that_sum_to(self.TEASPOONS, length=len(self.store.ingredients)):
            properties = tuple(
                sum(tsp * ing[prop] for tsp, ing in zip(teaspoons, self.store.ingredients))
                for prop in range(len(self.store.ingredients[0]))
            )
            if predicate(properties):
                score = reduce(lambda x, y: x * y, properties[:-1])
                highest_score = max(highest_score, score)
        return highest_score

    @staticmethod
    def nums_that_sum_to(target: int, length: int = 2) -> Generator[tuple[int, ...]]:
        """Returns a list of possible ways to"""
        if length == 1:
            yield (target,)
            return

        for i in range(1, target - length + 1):
            for tail in Day15.nums_that_sum_to(target - i, length - 1):
                yield (i,) + tail
