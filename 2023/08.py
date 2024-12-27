"""
--- Day 8: Haunted Wasteland ---
https://adventofcode.com/2023/day/8
"""

from math import lcm
from re import findall
from utils import *

args = parse_args(year=2023, day=8)
raw = get_input(args.filename, year=2023, day=8)

steps, paths = [group.splitlines() for group in raw.split("\n\n")]
steps = steps[0]

graph = {}
starts = []
for line in paths:
    n, l, r = findall(r"[A-Z0-9]{3}", line)
    graph[n] = {"L": l, "R": r}
    if n[-1] == "A":
        starts.append(n)

p1 = 0
curr = "AAA"
while curr != "ZZZ":
    curr = graph[curr][steps[p1 % len(steps)]]
    p1 += 1
print(p1)

sequences = []
for curr in starts:
    t = 0
    ends = []
    while len(ends) < 2:
        curr = graph[curr][steps[t % len(steps)]]
        if curr[-1] == "Z":
            ends.append(t)
        t += 1
    sequences.append(ends[1] - ends[0])

p2 = lcm(*sequences)
print(p2)

if args.test:
    args.tester(p1, p2)
