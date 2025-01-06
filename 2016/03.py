"""
--- Day 3: Squares With Three Sides ---
https://adventofcode.com/2016/day/3
"""

from utils import *

args = parse_args(year=2016, day=3)
raw = get_input(args.filename, year=2016, day=3)

triangles = [tuple(nums(line)) for line in raw.splitlines()]
p1 = sum(s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1 for s1, s2, s3 in triangles)
print(p1)

triangles = [i for t in list(zip(*[list(nums(line)) for line in raw.splitlines()])) for i in t]
p2 = sum(s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1 for s1, s2, s3 in chunks(triangles, n=3))
print(p2)

if args.test:
    args.tester(p1, p2)
