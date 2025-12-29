"""
--- Day 14: Reindeer Olympics ---
https://adventofcode.com/2015/day/14
"""

from advent.core import Solver


class Day14(Solver):
    """Solution for day 14."""

    def prepare(self) -> None:
        self.store.reindeer = list(self.utils.chunks(self.input.nums(), n=3))
        self.store.scores = [0] * len(self.store.reindeer)

    def part1(self) -> int:
        """Solve part 1."""
        longest = 0
        for t in range(1, 2504):
            dists = []
            for i, (vel, time, rest) in enumerate(self.store.reindeer):
                full_sprints = t // (time + rest)
                remaining = t - (time + rest) * full_sprints
                dist = vel * (time * full_sprints + min(remaining, time))
                dists.append(dist)
                if t == 2503:
                    longest = max(dist, longest)
            for i, dist in enumerate(dists):
                if dist == max(dists):
                    self.store.scores[i] += 1
        return longest

    def part2(self) -> int:
        """Solve part 2."""
        highest_score: int = max(self.store.scores)
        return highest_score
