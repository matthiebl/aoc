"""
--- Day 10: The Stars Align ---
https://adventofcode.com/2018/day/10
"""

from utils import *

args = parse_args(year=2018, day=10)
raw = get_input(args.filename, year=2018, day=10)


def coord_info(list):
    min_x = min(x for x, _ in list)
    min_y = min(y for _, y in list)
    max_x = max(x for x, _ in list)
    max_y = max(y for _, y in list)

    range_x = max_x - min_x
    range_y = max_y - min_y

    return min_x, min_y, max_x, max_y, range_x, range_y


lights = [tuple(nums(line)) for line in raw.splitlines()]

mr = float("inf")
p2 = None
for t in range(10000, 11000):
    min_x, min_y, max_x, max_y, range_x, range_y = coord_info([(x + dx * t, y + dy * t) for x, y, dx, dy in lights])
    if range_x + range_y < mr:
        mr, p2 = range_x + range_y, t

lights = [(x + dx * p2, y + dy * p2) for x, y, dx, dy in lights]

min_x, min_y, max_x, max_y, range_x, range_y = coord_info(lights)
grid = create_grid(range_y + 1, range_x + 1, fill=" ",
                   blocks=[(y - min_y, x - min_x, "\u2588") for x, y, in lights])
p1 = ["".join(r) for r in grid]
print("\n".join(p1))
print(p2)

if args.test:
    args.tester(p1, p2)
