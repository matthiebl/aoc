"""
--- Day 10: Syntax Scoring ---
https://adventofcode.com/2021/day/10
"""

from utils import *

args = parse_args(year=2021, day=10)
raw = get_input(args.filename, year=2021, day=10)

lines = raw.splitlines()

pair = {"(": ")", "[": "]", "{": "}", "<": ">"}
break_points = {")": 3, "]": 57, "}": 1197, ">": 25137}
close_points = {")": "1", "]": "2", "}": "3", ">": "4"}

close_scores = []

p1 = 0
for chunk in lines:
    stack = []
    for c in chunk:
        if c in pair:
            stack.append(pair[c])
        elif stack.pop() != c:
            p1 += break_points[c]
            break
    else:
        close_scores.append(int("".join(close_points[c] for c in stack[::-1]), 5))

print(p1)

p2 = sorted(close_scores)[len(close_scores) // 2]
print(p2)

if args.test:
    args.tester(p1, p2)
