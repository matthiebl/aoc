"""
--- Day 10: Knot Hash ---
https://adventofcode.com/2017/day/10
"""

from functools import reduce

from utils import *

args = parse_args(year=2017, day=10)
raw = get_input(args.filename, year=2017, day=10)

knot = list(range(256))
sizes = list(nums(raw))


def hash_round(i: int = 0, skip: int = 0):
    for size in sizes:
        mid = knot[i:i+size]
        if len(mid) < size:
            rem = size - len(mid)
            mid = (mid + knot[:rem])[::-1]
            knot[i:] = mid[:size-rem]
            knot[:rem] = mid[size-rem:]
        else:
            knot[i:i+size] = mid[::-1]
        i = (i + size + skip) % len(knot)
        skip = (skip + 1) % len(knot)
    return i, skip


hash_round()
p1 = knot[0] * knot[1]
print(p1)

knot = list(range(256))
sizes = list(map(ord, raw)) + [17, 31, 73, 47, 23]
i, skip = 0, 0
for _ in range(64):
    i, skip = hash_round(i, skip)
p2 = "".join(f"{hex(reduce(lambda x, y: x ^ y, ns[1:], ns[0]))[2:]:0>2}" for ns in chunks(knot, n=16))
print(p2)

if args.test:
    args.tester(p1, p2)
