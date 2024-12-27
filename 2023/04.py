"""
--- Day 4: Scratchcards ---
https://adventofcode.com/2023/day/4
"""

from collections import defaultdict
from utils import *

args = parse_args(year=2023, day=4)
raw = get_input(args.filename, year=2023, day=4)

cards = raw.splitlines()

p1 = 0
p2 = 0
copies = defaultdict(lambda: 1)

for i, card in enumerate(cards):
    left, right = card.split(" | ")
    winning = set(list(nums(left))[1:])
    yours = set(nums(right))
    match = len(winning.intersection(yours))
    if match:
        p1 += 2 ** (match - 1)
    p2 += copies[i]
    for j in range(i + 1, i + match + 1):
        copies[j] += copies[i]

print(p1)
print(p2)

if args.test:
    args.tester(p1, p2)
