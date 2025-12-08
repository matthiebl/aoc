"""
--- Day 8: Playground ---
https://adventofcode.com/2025/day/8
"""

from collections import Counter, defaultdict
from functools import reduce
from heapq import heappop, heappush
from math import sqrt

from advent.core import Solver


class Day08(Solver):
    """Solution for day 8."""
    NUM_SHORTEST = 1000
    N_LARGEST_TREES = 3

    def prepare(self):
        self.store.nodes = list(
            map(tuple, self.utils.chunks(self.input.nums(), n=3)))
        self.store.edges = []
        for i, n1 in enumerate(self.store.nodes):
            for n2 in self.store.nodes[i + 1:]:
                heappush(self.store.edges,
                         (self.euclidean_distance(n1, n2), n1, n2))

    @staticmethod
    def euclidean_distance(a: tuple[int, int, int], b: tuple[int, int, int]) -> int:
        x1, y1, z1 = a
        x2, y2, z2 = b
        return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)

    def get_forest_sizes_of_graph(self) -> list[int]:
        forest = {}
        tree_id = 0
        for node in self.store.graph:
            if node in forest:
                continue
            visited = set()
            search = [node]
            while search:
                node = search.pop()
                if node in visited:
                    continue
                visited.add(node)
                forest[node] = tree_id
                for adj in self.store.graph[node]:
                    if adj not in visited:
                        search.append(adj)

            tree_id += 1

        return sorted(Counter(forest.values()).values(), reverse=True)

    def part1(self) -> int:
        """Solve part 1."""

        self.store.graph = defaultdict(set)
        for _ in range(self.NUM_SHORTEST):
            _, n1, n2 = heappop(self.store.edges)
            self.store.graph[n1].add(n2)
            self.store.graph[n2].add(n1)

        sizes = self.get_forest_sizes_of_graph()[:self.N_LARGEST_TREES]
        return reduce(lambda x, y: x * y, sizes)

    def part2(self) -> int:
        """Solve part 2."""
        N = len(self.store.nodes)
        for _ in range(N - 1 - self.NUM_SHORTEST):
            _, n1, n2 = heappop(self.store.edges)
            self.store.graph[n1].add(n2)
            self.store.graph[n2].add(n1)

        while self.get_forest_sizes_of_graph()[0] != N:
            d, n1, n2 = heappop(self.store.edges)
            self.store.graph[n1].add(n2)
            self.store.graph[n2].add(n1)
            last_pair = n1[0] * n2[0]
        return last_pair
