"""
--- Day 6: Lanternfish ---
https://adventofcode.com/2021/day/6
"""

from collections import Counter

from utils import *

args = parse_args(year=2021, day=6)
raw = get_input(args.filename, year=2021, day=6)

lanternfish = Counter(nums(raw))

for day in range(256):
    if day == 80:
        p1 = sum(lanternfish.values())
    respawn = lanternfish.get(0, 0)
    for age in range(8):
        lanternfish[age] = lanternfish.get(age + 1, 0)
    lanternfish[6] = lanternfish.get(6, 0) + respawn
    lanternfish[8] = respawn

print(p1)

p2 = sum(lanternfish.values())
print(p2)

if args.test:
    args.tester(p1, p2)
