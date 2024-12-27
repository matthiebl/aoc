"""
--- Day 2: Cube Conundrum ---
https://adventofcode.com/2023/day/2
"""

from utils import *

args = parse_args(year=2023, day=2)
raw = get_input(args.filename, year=2023, day=2)

lines = raw.splitlines()
cubes = {"red": 12, "green": 13, "blue": 14}

p1, p2 = 0, 0
for game in lines:
    gid, rounds = game.split(": ")
    possible = True
    required = {"red": 0, "green": 0, "blue": 0}
    for round in rounds.split("; "):
        for cube in round.split(", "):
            amt, colour = cube.split(" ")
            if int(amt) > cubes[colour]:
                possible = False
            required[colour] = max(required[colour], int(amt))
    if possible:
        p1 += int(gid[5:])
    p2 += mul(n for n in required.values())

print(p1)
print(p2)

if args.test:
    args.tester(p1, p2)
