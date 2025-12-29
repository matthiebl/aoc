"""
--- Day 3: Lobby ---
https://adventofcode.com/2025/day/3
"""

from advent.core import Solver


class Day03(Solver):
    """Solution for day 3."""

    def prepare(self) -> None:
        self.store.banks = self.input.lines()

    def part1(self) -> int:
        """Solve part 1."""
        return sum(self.joltage(bank) for bank in self.store.banks)

    def part2(self) -> int:
        """Solve part 2."""
        return sum(self.joltage(bank, 12) for bank in self.store.banks)

    def joltage(self, bank: str, flips: int = 2) -> int:
        largest = list(map(int, bank[-flips:]))
        for n in map(int, bank[::-1][flips:]):
            if n >= largest[0]:
                # remove the first digit that breaks a non strict decreasing list,
                # otherwise the last digit
                new = [n]
                for i in range(flips - 1):
                    if largest[i] >= largest[i + 1]:
                        new.append(largest[i])
                    else:
                        new.extend(largest[i + 1 :])
                        break
                largest = new
        return int("".join(map(str, largest)))
