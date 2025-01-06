"""
--- Day 2: Bathroom Security ---
https://adventofcode.com/2016/day/2
"""

from utils import *

args = parse_args(year=2016, day=2)
raw = get_input(args.filename, year=2016, day=2)

instructions = raw.splitlines()

D = {
    "U": (-1, 0),
    "R": (0, 1),
    "D": (1, 0),
    "L": (0, -1)
}


def door_code(keypad: list[str]) -> int:
    code = ""
    r, c, = next(find_in_grid(keypad, "5"))
    for dirs in instructions:
        for d in dirs:
            dr, dc = D[d]
            if within_grid(keypad, r + dr, c + dc) and keypad[r + dr][c + dc] != ".":
                r, c = r + dr, c + dc
        code += keypad[r][c]
    return code


p1 = door_code(["123",
                "456",
                "789"])
print(p1)

p2 = door_code(["..1..",
                ".234.",
                "56789",
                ".ABC.",
                "..D.."])
print(p2)

if args.test:
    args.tester(p1, p2)
