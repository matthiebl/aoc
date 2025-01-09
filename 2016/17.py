"""
--- Day 17: Two Steps Forward ---
https://adventofcode.com/2016/day/17
"""

from _md5 import md5
from utils import *

args = parse_args(year=2016, day=17)
salt = get_input(args.filename, year=2016, day=17)


def traverse(size: int = 4, find_longest: bool = False):
    from collections import deque

    longest = 0
    pq = deque([(0, (0, 0), "")])
    while pq:
        d, (r, c), path = pq.popleft()

        if (r, c) == (size - 1, size - 1):
            if not find_longest:
                return path
            longest = max(longest, d)
            continue

        hash = md5(f"{salt}{path}".encode()).hexdigest()
        for direction, h, (dr, dc) in zip("UDLR", hash[:4], directions([1, 7, 3, 5])):
            nr, nc = r + dr, c + dc
            if 0 <= nr < size and 0 <= nc < size and h in "bcdef":
                pq.append((d + 1, (nr, nc), path + direction))

    return longest


p1 = traverse()
print(p1)

p2 = traverse(find_longest=True)
print(p2)

if args.test:
    args.tester(p1, p2)
