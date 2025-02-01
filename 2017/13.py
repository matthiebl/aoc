"""
--- Day 13: Packet Scanners ---
https://adventofcode.com/2017/day/13
"""

from utils import *

args = parse_args(year=2017, day=13)
raw = get_input(args.filename, year=2017, day=13)

scanners = list(chunks(nums(raw)))


def severity(delay: int = 0):
    caught = False
    score = 0
    for layer, depth in scanners:
        i = (layer + delay) % ((depth - 1) * 2)
        if i == 0:
            caught = True
            score += layer * depth
    return caught if delay else score


p1 = severity()
print(p1)

p2 = 1
while severity(p2):
    p2 += 1
print(p2)

if args.test:
    args.tester(p1, p2)
