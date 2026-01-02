"""
--- Day 22: Wizard Simulator 20XX ---
https://adventofcode.com/2015/day/22
"""

from dataclasses import astuple, dataclass, replace
from heapq import heappop, heappush

from advent.core import Solver


class Day22(Solver):
    """Solution for day 22."""

    def prepare(self) -> None:
        self.boss_health, self.boss_damage = self.input.nums()

    def part1(self) -> int:
        """Solve part 1."""
        return self.min_cost_to_win()

    def part2(self) -> int:
        """Solve part 2."""
        return self.min_cost_to_win(hard_mode=True)

    def min_cost_to_win(self, hard_mode: bool = False) -> int:
        visited = set()
        pq = [(0, self.GameState(boss_health=self.boss_health))]
        while pq:
            spent, state = heappop(pq)
            if astuple(state) in visited:
                continue
            visited.add(astuple(state))

            if state.player_turn and hard_mode:
                state.health -= 1
                if state.health <= 0:
                    continue

            armour = 0
            if state.poison:
                state.boss_health -= 3
                state.poison -= 1
            if state.shield:
                armour = 7
                state.shield -= 1
            if state.recharge:
                state.mana += 101
                state.recharge -= 1
            if state.is_boss_dead():
                return spent

            player_turn = state.player_turn
            state.player_turn = not player_turn
            if player_turn:
                if state.can_magic_missile():
                    next_state = state.use_magic_missile()
                    if next_state.is_boss_dead():
                        return spent + 53
                    heappush(pq, (spent + 53, next_state))
                if state.can_drain():
                    next_state = state.use_drain()
                    if next_state.is_boss_dead():
                        return spent + 73
                    heappush(pq, (spent + 73, next_state))
                if state.can_shield():
                    heappush(pq, (spent + 113, state.use_shield()))
                if state.can_poison():
                    heappush(pq, (spent + 173, state.use_poison()))
                if state.can_recharge():
                    heappush(pq, (spent + 229, state.use_recharge()))
            else:
                state.health -= max(self.boss_damage - armour, 1)
                if state.health > 0:
                    heappush(pq, (spent, state))

        raise RuntimeError("No minimum win condition for the player found")

    @dataclass(order=True)
    class GameState:
        boss_health: int
        health: int = 50
        mana: int = 500
        shield: int = 0
        poison: int = 0
        recharge: int = 0
        player_turn: bool = True

        def is_boss_dead(self) -> bool:
            return self.boss_health <= 0

        def can_magic_missile(self) -> bool:
            return self.mana >= 53

        def use_magic_missile(self) -> "Day22.GameState":
            return replace(self, boss_health=self.boss_health - 4, mana=self.mana - 53)

        def can_drain(self) -> bool:
            return self.mana >= 73

        def use_drain(self) -> "Day22.GameState":
            return replace(
                self, boss_health=self.boss_health - 2, health=self.health + 2, mana=self.mana - 73
            )

        def can_shield(self) -> bool:
            return self.mana >= 113 and self.shield == 0

        def use_shield(self) -> "Day22.GameState":
            return replace(self, mana=self.mana - 113, shield=6)

        def can_poison(self) -> bool:
            return self.mana >= 173 and self.poison <= 1

        def use_poison(self) -> "Day22.GameState":
            return replace(self, mana=self.mana - 173, poison=6)

        def can_recharge(self) -> bool:
            return self.mana >= 229 and self.recharge <= 1

        def use_recharge(self) -> "Day22.GameState":
            return replace(self, mana=self.mana - 229, recharge=5)
