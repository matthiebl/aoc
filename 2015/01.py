"""
--- Day 1: Not Quite Lisp ---
https://adventofcode.com/2015/day/1
"""

from utils import *

args = parse_args(year=2015, day=1)
moves = get_input(args.filename, year=2015, day=1)

floors = [0]
for move in moves:
    floors.append(floors[-1] + (1 if move == "(" else -1))

p1 = floors[-1]
p2 = floors.index(-1)
print(p1)
print(p2)

if args.test:
    args.tester(p1, p2)
