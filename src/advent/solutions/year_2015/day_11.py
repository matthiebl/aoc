"""
--- Day 11: Corporate Policy ---
https://adventofcode.com/2015/day/11
"""

from advent.core import Solver


class Day11(Solver):
    """Solution for day 11."""

    def prepare(self) -> None:
        self.store.password = self.input

    def part1(self) -> int:
        """Solve part 1."""
        while not self.valid_password(self.store.password):
            self.store.password = self.next_password(self.store.password)
        return self.store.password

    def part2(self) -> int:
        """Solve part 2."""
        self.store.password = self.next_password(self.store.password)
        while not self.valid_password(self.store.password):
            self.store.password = self.next_password(self.store.password)
        return self.store.password

    def next_password(self, password: str) -> str:
        last = password[-1]
        if last == "z":
            return self.next_password(password[:-1]) + "a"
        new = password[:-1] + chr(ord(last) + 1)
        if "i" in new or "o" in new or "l" in new:
            return self.next_password(new)
        return new

    def valid_password(self, password: str) -> bool:
        if not any("".join(seq) in password for seq in self.utils.windows(self.ALPHABET, 3)):
            return False
        if "i" in password or "o" in password or "l" in password:
            return False
        count = 0
        for c in self.ALPHABET:
            count += password.count(c + c)
        return count >= 2
