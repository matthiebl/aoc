"""
--- Day 12: ... ---
https://adventofcode.com/2017/day/12
"""

from collections import defaultdict

from utils import *

args = parse_args(year=2017, day=12)
raw = get_input(args.filename, year=2017, day=12)

pipes = {p: cs.split(", ") for p, cs in [line.split(" <-> ") for line in raw.splitlines()]}


def pipe_group(start: str = "0"):
    from collections import deque
    queue = deque([start])
    group = set()
    while queue:
        pipe = queue.popleft()
        if pipe in group:
            continue
        group.add(pipe)
        queue.extend(pipes[pipe])
    return group


group = pipe_group("0")
p1 = len(group)
print(p1)

p2 = 1
pipe_set = set(pipes) - group
while pipe_set:
    pipe_set -= pipe_group(pipe_set.pop())
    p2 += 1
print(p2)

if args.test:
    args.tester(p1, p2)
