"""
--- Day 18: Lavaduct Lagoon ---
https://adventofcode.com/2023/day/18

For part 1, a naive flood fill to find the area will work, but will not cut it for part 2.

In order to solve the larger example, we need to leverage the Shoelace formula, which has a nice general algorithm.
     n
    ___
    \
    /    (x_i . y_i+1  -  x_i+1 . y_i)
    ---
    i=1

This gives only the interior area, and in our case, the vertices used in the algorithm are at the center of each
perimeter wall, and not on the exterior.

So to add the part that's exterior, we also need to add the part on the outside. This will be half a block for every
straight edge. Plus the final 4 quarter blocks for the outside corners that get missed.

In order to add this extra part, I just added a unit for every up and right direction block, plus a final extra
unit for the quarters.
"""

from utils import *

args = parse_args(year=2023, day=18)
raw = get_input(args.filename, year=2023, day=18)

lines = list(map(lambda l: l.replace("(", "").replace(")", "").split(" "), raw.splitlines()))

D = {"R": (0, 1), "D": (1, 0), "L": (0, -1), "U": (-1, 0),
     "0": (0, 1), "1": (1, 0), "2": (0, -1), "3": (-1, 0)}


def shoelace(instructions: list[tuple[int | str, int]]):
    vertices = [(0, 0)]
    r, c = 0, 0
    for d, n in instructions:
        dr, dc = D[d]
        r, c = r + dr * n, c + dc * n
        vertices.append((r, c))
    vertices.append((0, 0))

    # shoelace formula
    interior = sum((c1 * r2) - (r1 * c2) for (r1, c1), (r2, c2) in windows(vertices))
    # extra exterior edges
    exterior = sum(n for d, n in instructions if d in ["U", "R", "0", "3"])
    return abs(interior) // 2 + exterior + 1


p1 = shoelace([(d, int(n)) for d, n, _ in lines])
print(p1)
p2 = shoelace([(hex[-1], int(hex[1:-1], 16)) for _, _, hex in lines])
print(p2)

if args.test:
    args.tester(p1, p2)
