#!/usr/bin/env python3.12

import aocutils as u
from sys import argv

from math import ceil

Blueprint = dict[str, dict[str, int]]

ORE = 0
CLAY = 1
OBSIDIAN = 2
GEODE = 3


blueprints: list[Blueprint] = []


def simulate(bp_id: int, best: list[int], cache: dict, time: int, resources, robots):
    blueprint = blueprints[bp_id]
    if time == 0:
        return resources[GEODE]

    if resources[GEODE] < best[time]:
        return resources[GEODE]
    best[time] = resources[GEODE]

    key = (time, *resources, *robots)
    if key in cache:
        return cache[key]

    # Do nothing, continue to produce geodes for the rest of the time
    max_geodes = time * robots[GEODE] + resources[GEODE]

    for i, bot_type in enumerate(['ore', 'clay', 'obsidian', 'geode']):
        if bot_type != 'geode' and robots[i] >= blueprint['max'][bot_type]:
            continue

        wait = 0
        for j, resource in enumerate(['ore', 'clay', 'obsidian']):
            if blueprint[bot_type][resource] == 0:
                continue
            if robots[j] == 0:
                break
            wait = max(wait, ceil(
                (blueprint[bot_type][resource] - resources[j]) / robots[j]))
        else:
            remaining = time - (wait + 1)
            if remaining <= 0:
                continue
            new_robots = robots[:]
            new_robots[i] += 1
            new_resources = [(wait + 1) * b + r for r,
                             b in zip(resources, robots)]
            for j, resource in enumerate(['ore', 'clay', 'obsidian']):
                new_resources[j] -= blueprint[bot_type][resource]
                new_resources[j] = min(
                    new_resources[j], blueprint['max'][resource] * remaining)
            max_geodes = max(max_geodes, simulate(
                bp_id, best, cache, remaining, new_resources, new_robots))

    cache[key] = max_geodes
    return max_geodes


def main(file: str) -> None:
    print('Day 19')

    def mapper(s: str) -> Blueprint:
        bp = u.find_digits(s)
        return {
            'ore': {'ore': bp[1], 'clay': 0, 'obsidian': 0},
            'clay': {'ore': bp[2], 'clay': 0, 'obsidian': 0},
            'obsidian': {'ore': bp[3], 'clay': bp[4], 'obsidian': 0},
            'geode': {'ore': bp[5], 'clay': 0, 'obsidian': bp[6]},
            'max': {
                'ore': max(bp[1], bp[2], bp[3], bp[5]),
                'clay': bp[4],
                'obsidian': bp[6],
            },
        }

    global blueprints
    blueprints = u.input_as_lines(file, map=mapper)

    p1 = 0
    for bp_id in range(len(blueprints)):
        res = simulate(bp_id, [0] * 25, {}, 24, [0, 0, 0, 0], [1, 0, 0, 0])
        p1 += res * (bp_id + 1)
    print(f'{p1=}')

    p2 = u.mul(simulate(bp_id, [0] * 33, {}, 32,
               [0, 0, 0, 0], [1, 0, 0, 0]) for bp_id in range(3))
    print(f'{p2=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '19.in'
    main(file)
