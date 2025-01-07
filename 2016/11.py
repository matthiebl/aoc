"""
--- Day 11: Radioisotope Thermoelectric Generators ---
https://adventofcode.com/2016/day/11
"""

from re import findall
from utils import *

args = parse_args(year=2016, day=11)
raw = get_input(args.filename, year=2016, day=11)

lines = raw.splitlines()

elements = []
floor_state: list[list] = []
for line in lines:
    floor_state.append([])
    for item in findall(r"([^ ]+ microchip|[^ ]+ generator)", line):
        if "microchip" in item:
            floor_state[-1].append((1, item[:item.index("-")]))
        else:
            floor_state[-1].append((-1, item.split()[0]))
            elements.append(item.split()[0])
floor_state = tuple(tuple(sorted(t * (elements.index(el) + 1) for t, el in floor)) for floor in floor_state)


def valid_floor(floor: tuple) -> bool:
    return not floor or not floor[-1] < 0 or all(-chip in floor for chip in floor if chip > 0)


def move_chips_and_generators(initial):
    from heapq import heappop, heappush
    from itertools import combinations

    seen = set()
    pq = [(0, 0, 0, initial)]
    while pq:
        _, steps, curr, floors = heappop(pq)
        key = (curr, floors)
        if key in seen:
            continue
        seen.add(key)
        if curr == 3 and all(len(f) == 0 for f in floors[:-1]):
            return steps

        for move in list(combinations(floors[curr], 1)) + list(combinations(floors[curr], 2)):
            for direction in [d for d in [-1, 1] if 0 <= d + curr < 4]:
                if curr + direction == 0 and not floors[0]:
                    continue
                new_floors = list(floors)
                new_floors[curr] = tuple(f for f in floors[curr] if f not in move)
                new_floors[curr + direction] = tuple(sorted(floors[curr + direction] + move))
                if not valid_floor(new_floors[curr]) or not valid_floor(new_floors[curr + direction]):
                    continue
                heuristic = sum(-i * 20 * len(f) for i, f in enumerate(new_floors))
                heappush(pq, (heuristic, steps + 1, curr + direction, tuple(new_floors)))


p1 = move_chips_and_generators(floor_state)
print(p1)

n = len(elements) + 1
floor_state = ((-n - 1, -n) + floor_state[0] + (n, n + 1), *floor_state[1:])
p2 = move_chips_and_generators(floor_state)
print(p2)

if args.test:
    args.tester(p1, p2)
