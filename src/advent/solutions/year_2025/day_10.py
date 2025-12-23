"""
--- Day 10: Factory ---
https://adventofcode.com/2025/day/10
"""

from dataclasses import dataclass
from heapq import heappop, heappush

import z3

from advent.core import Solver


class Day10(Solver):
    """Solution for day 10."""

    ON = "#"

    @dataclass
    class Machine:
        buttons: list[set[int]]
        lights: tuple[bool]
        joltage: tuple[int]

    def prepare(self):
        self.store.machines = []
        for line in self.input.lines():
            [raw_lights, *raw_buttons, raw_joltage] = line.split()
            buttons = list(map(lambda b: tuple(self.input.nums(b)), raw_buttons))
            lights = tuple(light == self.ON for light in raw_lights[1:-1])
            joltage = tuple(self.input.nums(raw_joltage))
            self.store.machines.append(self.Machine(buttons, lights, joltage))

    def part1(self) -> int:
        """Solve part 1."""
        return sum(self.presses_for_lights(machine) for machine in self.store.machines)

    def part2(self) -> int:
        """Solve part 2."""
        return sum(self.presses_for_joltage(machine) for machine in self.store.machines)

    def presses_for_lights(self, machine: Machine) -> int:
        seen_states = set()
        search = [(0, (False,) * len(machine.lights))]
        while search:
            presses, state = heappop(search)
            if state == machine.lights:
                return presses
            if state in seen_states:
                continue
            seen_states.add(state)
            for button in machine.buttons:
                new_state = tuple(
                    not light if i in button else light for i, light in enumerate(state)
                )
                if new_state not in seen_states:
                    heappush(search, (presses + 1, new_state))

    def presses_for_joltage(self, machine: Machine):
        s = z3.Optimize()
        vars = tuple(z3.Int(f"v{i}") for i in range(len(machine.buttons)))
        for v in vars:
            s.add(v >= 0)
        for i, joltage in enumerate(machine.joltage):
            equation = 0
            for j, button in enumerate(machine.buttons):
                if i in button:
                    equation += vars[j]
            s.add(equation == joltage)
        s.minimize(sum(vars))
        s.check()
        return s.model().eval(sum(vars)).as_long()
