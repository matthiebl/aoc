"""
--- Day 14: Reindeer Olympics ---
https://adventofcode.com/2015/day/14
"""

from utils import *

args = parse_args(year=2015, day=14)
raw = get_input(args.filename, year=2015, day=14)

reindeer = list(map(list, map(nums, raw.splitlines())))
scores = [0] * len(reindeer)

p1 = 0
for t in range(1, 2504):
    dists = []
    for i, (vel, time, rest) in enumerate(reindeer):
        full_sprints = t // (time + rest)
        remaining = t - (time + rest) * full_sprints
        dist = vel * (time * full_sprints + min(remaining, time))
        dists.append(dist)
        if t == 2503:
            p1 = max(dist, p1)
    for i, dist in enumerate(dists):
        if dist == max(dists):
            scores[i] += 1
print(p1)

p2 = max(scores)
print(p2)

if args.test:
    args.tester(p1, p2)
