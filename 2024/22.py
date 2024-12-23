"""
--- Day 22: Monkey Market ---
https://adventofcode.com/2024/day/22
"""

from collections import defaultdict, deque
from utils import *

args = parse_args(year=2024, day=22)
raw = get_input(args.filename, year=2024, day=22)

numbers = list(nums(raw))
bananas = defaultdict(int)

p1 = 0
for number in numbers:
    seen = set()
    changes = deque([])
    for i in range(2000):
        before = number % 10
        number = (number ^ (number << 6)) % 16777216
        number = (number ^ (number >> 5)) % 16777216
        number = (number ^ (number << 11)) % 16777216
        after = number % 10
        changes.append(after - before)
        if len(changes) == 4:
            key = tuple(changes)
            if key not in seen:
                bananas[tuple(changes)] += after
            seen.add(key)
            changes.popleft()
    p1 += number

p2 = max(v for v in bananas.values())
print(p1)
print(p2)

if args.test:
    args.tester(p1, p2)
