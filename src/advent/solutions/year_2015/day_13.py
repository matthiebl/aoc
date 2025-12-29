"""
--- Day 13: Knights of the Dinner Table ---
https://adventofcode.com/2015/day/13
"""

from collections import defaultdict
from itertools import permutations

from advent.core import Solver


class Day13(Solver):
    """Solution for day 13."""

    def prepare(self) -> None:
        self.store.people = defaultdict(lambda: defaultdict(int))

        desires = [line[:-1].split() for line in self.input.lines()]
        for [name, _, change, amt, *_, next_to] in desires:
            self.store.people[name][next_to] = int(amt) * (-1 if change == "lose" else 1)

    def part1(self) -> int:
        """Solve part 1."""
        return self.best_seating_score(self.store.people)

    def part2(self) -> int:
        """Solve part 2."""
        return self.best_seating_score(set(self.store.people) | {"Me"})

    def best_seating_score(self, names: set[str]) -> int:
        best = 0
        for arrangement in permutations(names):
            score = (
                self.store.people[arrangement[0]][arrangement[-1]]
                + self.store.people[arrangement[-1]][arrangement[0]]
            )
            for n1, n2 in self.utils.windows(arrangement):
                score += self.store.people[n1][n2] + self.store.people[n2][n1]
            best = max(score, best)
        return best
