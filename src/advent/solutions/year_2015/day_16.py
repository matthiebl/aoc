"""
--- Day 16: Aunt Sue ---
https://adventofcode.com/2015/day/16
"""

from advent.core import Solver


class Day16(Solver):
    """Solution for day 16."""

    READING = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1,
    }

    def prepare(self) -> None:
        self.sues = []
        for line in self.input.lines():
            raw_compounds = line[line.index(":") + 2 :].split(", ")
            self.sues.append({c: int(n) for c, n in map(lambda x: x.split(": "), raw_compounds)})

    def part1(self) -> int:
        """Solve part 1."""
        for i, sue in enumerate(self.sues, start=1):
            if all(self.READING[compound] == n for compound, n in sue.items()):
                return i
        raise RuntimeError("Reading does not match any Sue!")

    def part2(self) -> int:
        """Solve part 2."""
        for i, sue in enumerate(self.sues, start=1):
            for compound, n in sue.items():
                if compound in ["cats", "trees"]:
                    if n <= self.READING[compound]:
                        break
                elif compound in ["pomeranians", "goldfish"]:
                    if n >= self.READING[compound]:
                        break
                elif n != self.READING[compound]:
                    break
            else:
                return i
        raise RuntimeError("Reading does not match any Sue!")
