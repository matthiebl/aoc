"""
--- Day 17: Spinlock ---
https://adventofcode.com/2017/day/17
"""

from utils import *

args = parse_args(year=2017, day=17)
steps = int(get_input(args.filename, year=2017, day=17))

array = [0]
i = 0
for n in range(1, 2017 + 1):
    i = (i + steps) % n + 1
    array.insert(i, n)
p1 = array[(i + 1) % n]
print(p1)

p2 = None
i = 0
for n in range(1, 50000000 + 1):
    i = (i + steps) % n + 1
    if i == 1:
        p2 = n
print(p2)

if args.test:
    args.tester(p1, p2)
