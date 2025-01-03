"""
--- Day 16: Aunt Sue ---
https://adventofcode.com/2015/day/16
"""

from utils import *

args = parse_args(year=2015, day=16)
raw = get_input(args.filename, year=2015, day=16)

lines = raw.splitlines()
sues = [{it: int(v) for it, v in [it.split(": ") for it in line[line.index(":") + 2:].split(", ")]} for line in lines]

gift_sue = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}

for i, sue in enumerate(sues, start=1):
    if all(gift_sue[it] == v for it, v in sue.items()):
        p1 = i
        break
print(p1)

for i, sue in enumerate(sues, start=1):
    for it, v in sue.items():
        if it in ["cats", "trees"]:
            if gift_sue[it] >= v:
                break
        elif it in ["pomeranians", "goldfish"]:
            if gift_sue[it] <= v:
                break
        elif gift_sue[it] != v:
            break
    else:
        p2 = i
print(p2)

if args.test:
    args.tester(p1, p2)
