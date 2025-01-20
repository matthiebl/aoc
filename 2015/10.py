"""
--- Day 10: Elves Look, Elves Say ---
https://adventofcode.com/2015/day/10
"""

from itertools import groupby

from utils import *

args = parse_args(year=2015, day=10)
raw = get_input(args.filename, year=2015, day=10)


def look_and_say(code: str) -> str:
    said, cur, l = "", code[0], 1
    for nxt in code[1:]:
        if nxt == cur:
            l += 1
        else:
            said += f"{l}{cur}"
            cur, l = nxt, 1
    said += f"{l}{cur}"
    return said


code = raw
for _ in range(40):
    code = look_and_say(code)
p1 = len(code)
print(p1)

for _ in range(10):
    code = look_and_say(code)
p2 = len(code)
print(p2)

if args.test:
    args.tester(p1, p2)
