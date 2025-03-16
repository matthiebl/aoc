"""
--- Day 15: Beverage Bandits ---
https://adventofcode.com/2018/day/15
"""

from collections import deque

from utils import *

args = parse_args(year=2018, day=15)
raw = get_input(args.filename, year=2018, day=15)

grid = [list(line) for line in raw.splitlines()]
R, C = len(grid), len(grid[0])

spaces = {}
elves = {}
goblins = {}


def setup():
    spaces.clear()
    elves.clear()
    goblins.clear()
    for pos, v, _ in enumerate_grid(grid, skip="#"):
        spaces[pos] = v
        if v == "E":
            elves[pos] = 200
        elif v == "G":
            goblins[pos] = 200


def move(pos: tuple, type: str):
    enemy = "G" if type == "E" else "E"
    if any(spaces.get(tuple_add(pos, diff)) == enemy for diff in directions([1, 3, 5, 7])):
        return pos
    queue = deque([pos])
    visited = {pos}
    target = None
    while queue:
        r, c = queue.popleft()
        for dr, dc in directions([1, 3, 5, 7]):
            new_pos = r + dr, c + dc
            if spaces.get(new_pos) == "." and new_pos not in visited:
                queue.append(new_pos)
                visited.add(new_pos)
                if any(p != pos and spaces.get(p) == enemy for p in [tuple_add(new_pos, diff) for diff in directions([1, 3, 5, 7])]):
                    target = new_pos
                    break
        else:
            continue
        break
    if target is None:
        return pos

    queue = deque([target])
    visited = {target}
    choice = target if any(tuple_add(target, diff) == pos for diff in directions([1, 3, 5, 7])) else None
    while queue and choice is None:
        r, c = queue.popleft()
        for dr, dc in directions([1, 3, 5, 7]):
            new_pos = r + dr, c + dc
            if spaces.get(new_pos) == "." and new_pos not in visited:
                queue.append(new_pos)
                visited.add(new_pos)
                if any(tuple_add(new_pos, diff) == pos for diff in directions([1, 3, 5, 7])):
                    choice = new_pos
                    break
        else:
            continue
        break

    spaces[pos] = "."
    spaces[choice] = type
    type_collection = elves if type == "E" else goblins
    type_collection[choice] = type_collection[pos]
    del type_collection[pos]
    return choice


def attack(pos: tuple, type: str, damage: int = 3):
    enemy = "G" if type == "E" else "E"
    if not any(spaces.get(tuple_add(pos, diff)) == enemy for diff in directions([1, 3, 5, 7])):
        return
    enemy_collection = elves if enemy == "E" else goblins
    enemies = [(enemy_collection.get(p, 999), p) for p in [tuple_add(pos, diff) for diff in directions([1, 3, 5, 7])]]
    hp, p = sorted(enemies)[0]
    damage = 3 if type == "G" else damage
    enemy_collection[p] -= damage
    if hp <= damage:
        spaces[p] = "."
        del enemy_collection[p]


def turn(damage: int = 3):
    for (r, c), v in list(spaces.items()):
        if v == "." or spaces[(r, c)] != v:
            continue
        pos = move((r, c), v)
        attack(pos, v, damage)
        if not (elves and goblins):
            return False
    return elves and goblins


setup()
t = 0
while turn():
    t += 1
hp = sum(elves.values()) + sum(goblins.values())
p1 = t * hp
print(p1)


for damage in range(4, 100):
    setup()
    starting_elves = len(elves)
    t = 0
    while turn(damage) and len(elves) == starting_elves:
        t += 1
    if len(elves) == starting_elves:
        break

p2 = t * sum(elves.values())
print(p2)

if args.test:
    args.tester(p1, p2)
