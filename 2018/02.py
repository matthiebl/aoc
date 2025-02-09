"""
--- Day 2: Inventory Management System ---
https://adventofcode.com/2018/day/2
"""

from collections import Counter
from functools import cmp_to_key

from utils import *

args = parse_args(year=2018, day=2)
raw = get_input(args.filename, year=2018, day=2)

boxes = raw.splitlines()

twos, threes = 0, 0
for box_id in boxes:
    counts = Counter(box_id).values()
    if 2 in counts:
        twos += 1
    if 3 in counts:
        threes += 1

p1 = twos * threes
print(p1)

for i, id_a in enumerate(boxes):
    for id_b in boxes[i+1:]:
        if sum(a != b for a, b in zip(id_a, id_b)) == 1:
            p2 = "".join(a for a, b in zip(id_a, id_b) if a == b)
            break
    else:
        continue
    break
print(p2)

if args.test:
    args.tester(p1, p2)
