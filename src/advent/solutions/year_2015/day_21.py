"""
--- Day 21: RPG Simulator 20XX ---
https://adventofcode.com/2015/day/21
"""

from collections.abc import Generator
from functools import cache

from advent.core import Solver


class Day21(Solver):
    """Solution for day 21."""

    WEAPONS = [
        (8, 4, 0),
        (10, 5, 0),
        (25, 6, 0),
        (40, 7, 0),
        (74, 8, 0),
    ]
    ARMOURS = [
        (0, 0, 0),
        (13, 0, 1),
        (31, 0, 2),
        (53, 0, 3),
        (75, 0, 4),
        (102, 0, 5),
    ]
    RINGS = [
        (0, 0, 0),
        (0, 0, 0),
        (25, 1, 0),
        (50, 2, 0),
        (100, 3, 0),
        (20, 0, 1),
        (40, 0, 2),
        (80, 0, 3),
    ]

    def prepare(self) -> None:
        self.health, self.damage, self.armour = self.input.nums()

    def part1(self) -> float:
        """Solve part 1."""
        min_cost = float("inf")
        for wins, cost in self.game_outcomes():
            if wins:
                min_cost = min(min_cost, cost)
        return min_cost

    def part2(self) -> float:
        """Solve part 2."""
        max_cost = 0
        for wins, cost in self.game_outcomes():
            if not wins:
                max_cost = max(max_cost, cost)
        return max_cost

    def game_outcomes(self) -> Generator[tuple[bool, int]]:
        for weapon_cost, damage, _ in self.WEAPONS:
            for armour_cost, _, armour in self.ARMOURS:
                for i, (ring1_cost, ring1_damage, ring1_armour) in enumerate(self.RINGS):
                    for ring2_cost, ring2_damage, ring2_armour in self.RINGS[i + 1 :]:
                        wins = self.does_player_win(
                            damage + ring1_damage + ring2_damage,
                            armour + ring1_armour + ring2_armour,
                        )
                        yield wins, weapon_cost + armour_cost + ring1_cost + ring2_cost

    @cache
    def does_player_win(self, damage: int, attack: int, player_health: int = 100) -> bool:
        player_damage = max(damage - self.armour, 1)
        enemy_damage = max(self.damage - attack, 1)
        enemy_health = self.health
        while True:
            enemy_health -= player_damage
            if enemy_health <= 0:
                return True
            player_health -= enemy_damage
            if player_health <= 0:
                return False
