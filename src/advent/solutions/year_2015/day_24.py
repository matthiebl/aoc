"""
--- Day 24: It Hangs in the Balance ---
https://adventofcode.com/2015/day/24

The solution here reuses the same logic from day 17 of this year. We first start by realising that
for each compartment to have the same weight, they must each weigh `total-weight / num-of-presents`.
Now we have a target weight, and the list of weights, we can reuse the liquid container problem from
day 17 which had us find ways of using containers to reach the target.

We have the same problem here, but now are only really concerned with the presents in the
compartment Santa is in. The other compartments will have some irrelevant combination of presents
that sum to our target, but we do not need that information.

To search all ways of taking presents to reach our target weight is somewhat slow, but by using a
global minimum number of presents we have already found, we can quit early on the combinations that
are already worse that our best. This cuts it down from ~6 => <1 seconds. Next we just need to keep
track of the best quantum entanglement every time we see our current minimum number of presents.
"""

from collections import defaultdict

from advent.core import Solver


class Day24(Solver):
    """Solution for day 24."""

    def prepare(self) -> None:
        self.weights = self.input.nums()
        self.smallest = float("inf")

    def part1(self) -> float:
        """Solve part 1."""
        return self.present_entanglement(sum(self.weights) // 3)

    def part2(self) -> float:
        """Solve part 2."""
        return self.present_entanglement(sum(self.weights) // 4)

    def present_entanglement(
        self,
        target: int,
        total: int = 0,
        taken: float = 0,
        i: int = 0,
        quantum: int = 1,
        entanglement: dict[float, float] = defaultdict(lambda: float("inf")),
    ) -> float:
        if total > target or taken > self.smallest:
            return entanglement[self.smallest]

        if i == len(self.weights):
            if total == target and taken <= self.smallest:
                self.smallest = min(self.smallest, taken)
                entanglement[taken] = min(entanglement[taken], quantum)
            return entanglement[self.smallest]

        self.present_entanglement(
            target,
            total + self.weights[i],
            taken + 1,
            i + 1,
            quantum * self.weights[i],
            entanglement,
        )
        self.present_entanglement(target, total, taken, i + 1, quantum, entanglement)

        return entanglement[self.smallest]
