"""
--- Day 9: All in a Single Night ---
https://adventofcode.com/2015/day/9
"""

from collections import defaultdict

from advent.core import Solver


class Day09(Solver):
    """Solution for day 9."""

    def prepare(self):
        self.store.graph = defaultdict(list)
        for line in self.input.lines():
            a, _, b, _, n = line.split()
            self.store.graph[a].append((int(n), b))
            self.store.graph[b].append((int(n), a))

    def part1(self) -> int:
        """Solve part 1."""
        distance = float("inf")
        for n in self.store.graph:
            stack = [(0, n, set())]
            while stack:
                d, nxt, visited = stack.pop()
                if nxt in visited:
                    continue
                visited.add(nxt)

                if len(visited) == len(self.store.graph):
                    distance = min(distance, d)
                stack.extend([(d + w, pos, set(visited)) for w, pos in self.store.graph[nxt]])
        return distance

    def part2(self) -> int:
        """Solve part 2."""
        distance = 0
        for n in self.store.graph:
            stack = [(0, n, set())]
            while stack:
                d, nxt, visited = stack.pop()
                if nxt in visited:
                    continue
                visited.add(nxt)

                if len(visited) == len(self.store.graph):
                    distance = max(distance, d)
                stack.extend([(d + w, pos, set(visited)) for w, pos in self.store.graph[nxt]])
        return distance
