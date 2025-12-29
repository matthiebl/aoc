"""
--- Day 9: All in a Single Night ---
https://adventofcode.com/2015/day/9
"""

from collections import defaultdict
from collections.abc import Callable

from advent.core import Solver


class Day09(Solver):
    """Solution for day 9."""

    def prepare(self) -> None:
        self.store.graph = defaultdict(list)
        for line in self.input.lines():
            a, _, b, _, n = line.split()
            self.store.graph[a].append((int(n), b))
            self.store.graph[b].append((int(n), a))

    def part1(self) -> float:
        """Solve part 1."""
        return self.path_distance(using=min, start=float("inf"))

    def part2(self) -> float:
        """Solve part 2."""
        return self.path_distance(using=max)

    def path_distance(self, using: Callable[[float, float], float], start: float = 0) -> float:
        distance = start
        for n in self.store.graph:
            stack: list[tuple[int, int, set[int]]] = [(0, n, set())]
            while stack:
                d, nxt, visited = stack.pop()
                if nxt in visited:
                    continue
                visited.add(nxt)

                if len(visited) == len(self.store.graph):
                    distance = using(distance, d)
                stack.extend([(d + w, pos, set(visited)) for w, pos in self.store.graph[nxt]])
        return distance
