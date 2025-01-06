"""
--- Day 21: RPG Simulator 20XX ---
https://adventofcode.com/2015/day/21
"""

from utils import *

args = parse_args(year=2015, day=21)
raw = get_input(args.filename, year=2015, day=21)

health, damage, armour = nums(raw)


def does_player_win(d: int, a: int, hp: int = 100):
    player_damage = max(d - armour, 1)
    enemy_damage = max(damage - a, 1)
    enemy = health
    player = hp
    while True:
        enemy -= player_damage
        if enemy <= 0:
            return True
        player -= enemy_damage
        if player <= 0:
            return False


weapons = [(8, 4, 0), (10, 5, 0), (25, 6, 0), (40, 7, 0), (74, 8, 0)]
armours = [(0, 0, 0), (13, 0, 1), (31, 0, 2), (53, 0, 3), (75, 0, 4), (102, 0, 5)]
rings = [(0, 0, 0), (0, 0, 0), (25, 1, 0), (50, 2, 0), (100, 3, 0), (20, 0, 1), (40, 0, 2), (80, 0, 3)]

p1 = float("inf")
p2 = 0
for wc, wd, wa in weapons:
    for ac, ad, aa, in armours:
        for r, (r1c, r1d, r1a) in enumerate(rings):
            for r2c, r2d, r2a in rings[r + 1:]:
                if does_player_win(wd + ad + r1d + r2d, wa + aa + r1a + r2a):
                    p1 = min(p1, wc + ac + r1c + r2c)
                else:
                    p2 = max(p2, wc + ac + r1c + r2c)
print(p1)
print(p2)

if args.test:
    args.tester(p1, p2)
