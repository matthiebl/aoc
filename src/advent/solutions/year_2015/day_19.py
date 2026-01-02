"""
--- Day 19: Medicine for Rudolph ---
https://adventofcode.com/2015/day/19
"""

from re import sub

from advent.core import Solver


class Day19(Solver):
    """Solution for day 19."""

    def prepare(self) -> None:
        replacements, molecule = self.input.sections()
        self.replacements = [replacement.split(" => ") for replacement in replacements.lines()]
        self.molecule = molecule

    def part1(self) -> int:
        """Solve part 1."""
        molecules = {
            self.molecule[:i] + sub(search, repl, self.molecule[i:], count=1)
            for i in range(len(self.molecule))
            for search, repl in self.replacements
        } - {self.molecule}
        return len(molecules)

    def part2(self) -> int:
        """Solve part 2."""
        return (
            sum(e == e.upper() for e in self.molecule)
            - self.molecule.count("Rn")
            - self.molecule.count("Ar")
            - 2 * self.molecule.count("Y")
            - 1
        )
