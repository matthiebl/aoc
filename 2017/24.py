"""
--- Day 24: Electromagnetic Moat ---
https://adventofcode.com/2017/day/24
"""

from collections import deque

from utils import *

args = parse_args(year=2017, day=24)
raw = get_input(args.filename, year=2017, day=24)

components = [tuple(nums(line)) for line in raw.splitlines()]

longest = 0
p1 = 0
p2 = 0
queue = deque([(0, sum(comp), sum(comp), {i}) for i, comp in enumerate(components) if 0 in comp])
while queue:
    length, strength, nxt, used = queue.popleft()
    p1 = max(p1, strength)
    if length == longest:
        p2 = max(p2, strength)
    elif length > longest:
        longest = length
        p2 = strength

    for i, comp in enumerate(components):
        if nxt in comp and i not in used:
            queue.append((length + 1, strength + sum(comp), sum(comp) - nxt, used.union({i})))
print(p1)
print(p2)

if args.test:
    args.tester(p1, p2)
