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
initial: list[list] = []
for line in lines:
    initial.append([])
    for item in findall(r"([^ ]+ microchip|[^ ]+ generator)", line):
        if "microchip" in item:
            initial[-1].append((1, item[:item.index("-")]))
        else:
            initial[-1].append((-1, item.split()[0]))
            elements.append(item.split()[0])
initial = tuple(tuple(sorted(t * (elements.index(el) + 1) for t, el in floor)) for floor in initial)


def floor_valid(floor: tuple) -> bool:
    return not floor or not floor[-1] < 0 or all(-chip in floor for chip in floor if chip > 0)


def move_things():
    from heapq import heappop, heappush
    from itertools import combinations

    seen = set()
    pq = [(0, 0, initial)]
    while pq:
        steps, curr, floors = heappop(pq)
        key = (curr, floors)
        if key in seen:
            continue
        seen.add(key)
        # print(steps, key)
        if curr == 3 and all(len(f) == 0 for f in floors[:-1]):
            return steps

        for move in list(combinations(floors[curr], 1)) + list(combinations(floors[curr], 2)):
            for direction in [d for d in [-1, 1] if 0 <= d + curr < 4]:
                new_floors = list(floors)
                new_floors[curr] = tuple(f for f in floors[curr] if f not in move)
                new_floors[curr + direction] = tuple(sorted(floors[curr + direction] + move))
                if not floor_valid(new_floors[curr]) or not floor_valid(new_floors[curr + direction]):
                    continue
                heappush(pq, (steps + 1, curr + direction, tuple(new_floors)))


        continue
        for i, (ta, na) in enumerate(floor):
            new_floors = [f1, f2, f3, f4]
            new_floors[curr] = [t for t in floor if t not in [(ta, na)]]
            if not valid_floor(new_floors[curr]):
                continue
            for j in [-1, 1]:
                if 0 <= curr + j < 4:
                    next_floor = [*new_floors[curr + j], (ta, na)]
                    if valid_floor(next_floor):
                        heappush(pq, (steps + 1, curr + j, *[next_floor if k == curr + j else f for k, f in enumerate(new_floors)]))
            for (tb, nb) in floor[i + 1:]:
                if ta != tb and na != nb:
                    continue
                new_floors = [f1, f2, f3, f4]
                new_floors[curr] = [t for t in floor if t not in [(ta, na), (tb, nb)]]
                if not valid_floor(new_floors[curr]):
                    continue
                for j in [-1, 1]:
                    # if j == -1 and curr == 1 and not f1:
                    #     continue
                    # if j == -1 and curr == 2 and not f1 and not f2:
                    #     continue
                    if 0 <= curr + j < 4:
                        next_floor = [*new_floors[curr + j], (ta, na), (tb, nb)]
                        if valid_floor(next_floor):
                            heappush(pq, (steps + 1, curr + j, *[next_floor if k == curr + j else f for k, f in enumerate(new_floors)]))


p1 = move_things()
p2 = 0


print(p1)
# print(p2)

if args.test:
    args.tester(p1, p2)
