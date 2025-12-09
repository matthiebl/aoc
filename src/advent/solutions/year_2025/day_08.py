"""
--- Day 8: Playground ---
https://adventofcode.com/2025/day/8
"""

from functools import reduce
from heapq import heappop, heappush

from advent.core import Solver


class DisjointSet:
    def __init__(self, n_ids):
        self.parent = list(range(n_ids))
        self.size = [1] * n_ids
        self.is_root = [True] * n_ids

    def find(self, x):
        if self.parent[x] == x:
            return x
        return self.find(self.parent[x])

    def union(self, x, y):
        a = self.find(x)
        b = self.find(y)
        if a == b:
            return
        if self.size[a] < self.size[b]:
            a, b = b, a
        self.parent[b] = a
        self.size[a] += self.size[b]
        self.is_root[b] = False

    def root_size(self, x):
        return self.size[self.find(x)]

    def root_sizes(self):
        return [self.size[i] for i, root in enumerate(self.is_root) if root]


class Day08(Solver):
    """Solution for day 8."""

    NUM_SHORTEST = 1000
    N_LARGEST_TREES = 3

    def prepare(self):
        self.store.nodes = list(map(tuple, self.utils.chunks(self.input.nums(), n=3)))
        self.store.edges = []
        for i, n1 in enumerate(self.store.nodes):
            for n2 in self.store.nodes[i + 1 :]:
                heappush(
                    self.store.edges, (self.utils.euclidean_distance(n1, n2, relative=True), n1, n2)
                )
        self.store.ids = {n: i for i, n in enumerate(self.store.nodes)}

    def part1(self) -> int:
        """Solve part 1."""
        ds = DisjointSet(len(self.store.nodes))

        edges = self.store.edges.copy()
        for _ in range(self.NUM_SHORTEST):
            _, n1, n2 = heappop(edges)
            ds.union(self.store.ids[n1], self.store.ids[n2])

        sizes = sorted(ds.root_sizes())[-self.N_LARGEST_TREES :]
        return reduce(lambda x, y: x * y, sizes)

    def part2(self) -> int:
        """Solve part 2."""
        ds = DisjointSet(len(self.store.nodes))
        edges = self.store.edges.copy()

        while len(ds.root_sizes()) > 1:
            _, n1, n2 = heappop(edges)
            ds.union(self.store.ids[n1], self.store.ids[n2])
            last_pair = n1[0] * n2[0]

        return last_pair
