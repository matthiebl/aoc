"""
--- Day 2: ... ---
https://adventofcode.com/2025/day/2
"""

from utils import *

args = parse_args(year=2025, day=2)
raw = get_input(args.filename, year=2025, day=2)

ranges = raw.split(",")

p1 = 0
p2 = 0

for r in ranges:
    [a, b] = list(map(int, r.split("-")))
    for n in range(a, b + 1):
        id_ = str(n)
        length = len(id_)
        if length % 2 == 0 and id_[:length//2] == id_[length//2:]:
            p1 += n
        for l in range(1, length // 2 + 1):
            if id_ == (id_[:l] * (length // l)):
                p2 += n
                break

print(p1)
print(p2)

if args.test:
    args.tester(p1, p2)
