"""
--- Day 22: Sand Slabs ---
https://adventofcode.com/2023/day/22
"""

from collections import defaultdict

from utils import *

args = parse_args(year=2023, day=22)
raw = get_input(args.filename, year=2023, day=22)

blocks = sorted((tuple(nums(line)) for line in raw.splitlines()), key=lambda l: l[2])

# Move all bricks down
max_height = defaultdict(int)
for i, (x1, y1, z1, x2, y2, z2) in enumerate(blocks):
    z = max(max_height[(x, y)] for x in range(x1, x2 + 1) for y in range(y1, y2 + 1)) + 1
    max_height.update({(x, y): z + z2 - z1 for x in range(x1, x2 + 1) for y in range(y1, y2 + 1)})
    blocks[i] = (x1, y1, z, x2, y2, z + z2 - z1)

cubes = {(x, y, z): i for i, (x1, y1, z1, x2, y2, z2) in enumerate(blocks)
         for x in range(x1, x2 + 1) for y in range(y1, y2 + 1) for z in range(z1, z2 + 1)}

# Determine what bricks are above and below every brick
above = defaultdict(set)
below = defaultdict(set)
for (x, y, z), i in cubes.items():
    j = cubes.get((x, y, z + 1), i)
    if j != i:
        above[i].add(j)
    j = cubes.get((x, y, z - 1), i)
    if j != i:
        below[i].add(j)


def how_many_fall(brick: int) -> int:
    fallen = set()
    q = [brick]
    while q:
        brick = q.pop(0)
        fallen.add(brick)
        for b in above[brick]:
            if len(below[b] - fallen) == 0:
                q.append(b)
    return len(fallen) - 1


p1 = sum(how_many_fall(i) == 0 for i in range(len(blocks)))
print(p1)

p2 = sum(how_many_fall(i) for i in range(len(blocks)))
print(p2)

if args.test:
    args.tester(p1, p2)
