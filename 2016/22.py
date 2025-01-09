"""
--- Day 22: Grid Computing ---
https://adventofcode.com/2016/day/22

This problem sounds scary to solve in the general case, but once you look at the input, solving the problem is
somewhat trivial.

The input grid, looks something like the below representation. You have the goal at the top right, and a wall of
immovable nodes (ie. nodes with data too large to fit anywhere else) two rows below that extends from the right
wall to the left. The empty node is then somewhere below that wall.

(.). . . . . . . . . . . . . . . . . . G
 . . . . . . . . . . . . . . . . . . . .
 . . . . . . . . . # # # # # # # # # # #
 . . . . . . . . . . . . . . . . . . . .
 . . . . . . . . . . . . . _ . . . . . .

In order to find the moves it takes to get G to the start, we start my moving the empty node to the column left of
the wall, and then to the top row. Then we proceed by moving the empty node all the way to the right, so we get
to the following scenario.

(.). . . . . . . . . . . . . . . . . G _
 . . . . . . . . . . . . . . . . . . . .

From here we just want to move the G all the way left. In order to move the G one step left, we have to move the
empty node in a loop (as shown in the AoC example) of 5 steps, and repeat until we are all the way left.
"""

from utils import *

args = parse_args(year=2016, day=22)
raw = get_input(args.filename, year=2016, day=22)

nodes = [(x, y, used, avail) for x, y, _, used, avail, _ in [tuple(nums(line)) for line in raw.splitlines()[2:]]]

ex, ey, empty_avail = next((x, y, avail) for x, y, used, avail in nodes if used == 0)
movable = {(x, y) for x, y, used, _ in nodes if used <= empty_avail and used != 0}
p1 = len(movable)
print(p1)

# (gx, 0) is the goal node we want to move to the top left
gx = nodes[-1][0]
immovable = {(x, y) for x, y, used, _ in nodes if used > empty_avail and used != 0}
# (ix, iy) is the top-left most block that is too large to move
_, ix, iy = min(((gx + 1) * y + x, x, y) for x, y in immovable)

p2 = manhattan(ex, ey, ix - 1, 0) + abs(ix - 1 - gx) + 5 * (gx - 1)
print(p2)

if args.test:
    args.tester(p1, p2)
