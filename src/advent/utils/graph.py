"""Graph utilities"""

from collections import defaultdict
from dataclasses import dataclass


class Graph[T]:
    """Graph operations"""

    def __init__(self) -> None:
        self.nodes: set[T] = set()
        self.edges: dict[T, list[Graph.Edge]] = defaultdict(list[Graph.Edge[T]])

    def add_node(self, v: T) -> None:
        self.nodes.add(v)

    def add_edge(self, v: T, w: T, cost: float = 1) -> None:
        self.add_node(v)
        self.add_node(w)
        self.edges[v].append(Graph.Edge(v, w, cost))

    @dataclass
    class Edge[U]:
        origin: U
        to: U
        cost: float = 1
