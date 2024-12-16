"""
--- Day 14: Restroom Redoubt ---
https://adventofcode.com/2024/day/14
"""

from utils import *

args = parse_args(year=2024, day=14)
raw = get_input(args.filename, year=2024, day=14)

robots = [tuple(nums(line))[::-1] for line in raw.splitlines()]
R, C = 103, 101

robots_100 = []
for vr, vc, pr, pc in robots:
    robots_100.append(((pr + 100 * vr) % R, (pc + 100 * vc) % C))

q1 = sum([1 for r, c in robots_100 if r < R // 2 and c < C // 2])
q2 = sum([1 for r, c in robots_100 if r > R // 2 and c < C // 2])
q3 = sum([1 for r, c in robots_100 if r < R // 2 and c > C // 2])
q4 = sum([1 for r, c in robots_100 if r > R // 2 and c > C // 2])

p1 = mul(q1, q2, q3, q4)
print(p1)

num_robots = len(robots)
p2 = 0
while len(set((r, c) for _, _, r, c in robots)) != num_robots:
    robots = [(vr, vc, (pr + vr) % R, (pc + vc) % C) for vr, vc, pr, pc in robots]
    p2 += 1
print(p2)

if args.test:
    args.tester(p1, p2)
