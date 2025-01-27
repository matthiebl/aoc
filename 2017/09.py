"""
--- Day 9: Stream Processing ---
https://adventofcode.com/2017/day/9
"""

from utils import *

args = parse_args(year=2017, day=9)
stream = get_input(args.filename, year=2017, day=9)

p1, p2 = 0, 0
depth = 0
garbage = False
while stream:
    if not garbage and stream[0] == "{":
        depth = depth + 1
    elif not garbage and stream[0] == "}":
        depth, p1 = depth - 1, p1 + depth
    elif not garbage and stream[0] == "<":
        garbage = True
    elif garbage and stream[0] == ">":
        garbage = False
    elif garbage and stream[0] == "!":
        stream = stream[1:]
    elif garbage:
        p2 += 1
    stream = stream[1:]

print(p1)
print(p2)

if args.test:
    args.tester(p1, p2)
