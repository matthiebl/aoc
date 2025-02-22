"""
--- Day 14: Chocolate Charts ---
https://adventofcode.com/2018/day/14
"""

from utils import *

args = parse_args(year=2018, day=14)
raw = get_input(args.filename, year=2018, day=14)

length = len(raw)
goal = list(map(int, raw))
recipes = int(raw)

scores = [3, 7]

elf1, elf2 = 0, 1
p1, p2 = None, None
while p1 is None or p2 is None:
    if p1 is None and len(scores) >= recipes + 10:
        p1 = "".join(map(str, scores[recipes:recipes + 10]))

    for i in str(scores[elf1] + scores[elf2]):
        scores.append(int(i))
        if p2 is None and scores[-length:] == goal:
            p2 = len(scores) - length

    elf1 = (elf1 + scores[elf1] + 1) % len(scores)
    elf2 = (elf2 + scores[elf2] + 1) % len(scores)

print(p1)
print(p2)

if args.test:
    args.tester(p1, p2)
