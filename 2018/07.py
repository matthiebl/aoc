"""
--- Day 7: The Sum of Its Parts ---
https://adventofcode.com/2018/day/7
"""

from collections import defaultdict

from utils import *

args = parse_args(year=2018, day=7)
raw = get_input(args.filename, year=2018, day=7)

input = defaultdict(set)
output = defaultdict(set)
for line in raw.splitlines():
    b, a = line[5], line[36]
    input[a].add(b)
    output[b].add(a)

steps = ""
queue = sorted(c for c in "QWERTYUIOPASDFGHJKLZXCVBNM" if c not in input)
while queue:
    for c in queue:
        if not input[c] - set(steps):
            break
    queue.remove(c)
    steps += c
    for c in output[c]:
        if c not in steps and c not in queue:
            queue.append(c)
    queue = sorted(queue)

p1 = steps
p2 = 0


print(p1)
# print(p2)

if args.test:
    args.tester(p1, p2)
