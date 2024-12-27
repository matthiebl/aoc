"""
--- Day 6: Wait For It ---
https://adventofcode.com/2023/day/6
"""

from utils import *

args = parse_args(year=2023, day=6)
raw = get_input(args.filename, year=2023, day=6)

times, distances = list(map(list, map(nums, raw.splitlines())))

p1 = 1
for time, dist in zip(times, distances):
    p1 *= sum(1 for t in range(time + 1) if t * (time - t) > dist)
print(p1)

# Use binary search to find lowest time that still beats the record
time, dist = tuple(nums(raw.replace(" ", "")))
lo, hi = 1, time // 2
while lo < hi:
    m = (lo + hi) // 2
    if m * (time - m) > dist:
        hi = m
    else:
        lo = m + 1

p2 = (1 if (time // 2) % 2 == 0 else 0) + 2 * (time // 2 - lo)
print(p2)

if args.test:
    args.tester(p1, p2)
