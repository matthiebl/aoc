#!/usr/bin/env python3.12

import aocutils as u
from sys import argv

"""
--- Day 18: Lavaduct Lagoon ---

Oh boy, was this a more difficult problem than I wanted.
At least is was an appropriately placed day.

I tried a few things to solve this problem.

Initially, I used a floodfill for part 1, but this was obviously
not going to work for part 2.

So I tried another idea I had for day 10, where you could move
along a row/column and work out based on the types of edges, which
part of the shape was inside or outside. This proved difficult,
and I was getting incorrect answers.

I even tried to implement a strategy that was analagous to working
out the integrals of each horizontal line, adding/subtracting the
different direction lines. This was also not working for me.

Finally, after admitting defeat, I tried having a look for
existing algorithms that could solve the problem for me.

I found the Shoelace formula, which had a nice simple general
algorithm.
     n
    ___
    \
    /    (x_i . y_i+1  -  x_i+1 . y_i)
    ---
    i=1

This gives only the interior area, and in our case, the vertices
used in the algorithm are at the center of each perimeter wall,
and not on the exterior.

So to add the part that's exterior, we also need to add the part on
the outside. This will be half a block for every straight edge.
Plus the final 4 quarter blocks for the outside corners that get
missed.

In order to add this extra part, I just added a unit for every
up and right direction block, plus a final extra unit for the quarters.
"""

DX = [0, 1, 0, -1]
DY = [-1, 0, 1, 0]
DD = {'U': 0, 'R': 1, 'D': 2, 'L': 3}


def instructions_to_vertices(instructions):
    pos = (0, 0)
    vertices = [pos]
    for d, dist in instructions:
        pos = u.add_tup(pos, u.mul_tup((DX[d], DY[d]), dist))
        vertices.append(pos)
    return vertices


def area(instructions):
    vertices = instructions_to_vertices(instructions)

    instructions.append(instructions[0])
    exterior = 0
    for d1, dst1 in instructions:
        # up and right blocks
        if d1 == 0 or d1 == 1:
            exterior += dst1

    # Shoelace interior area
    interior = 0
    for (x1, y1), (x2, y2) in zip(vertices, vertices[1:]):
        interior += (x1 * y2) - (x2 * y1)
    interior = abs(interior) // 2

    # the above, plus a final block
    return (exterior + interior + 1)


def main(file: str) -> None:
    print('Day 18')

    raw = u.input_as_lines(file, map=lambda l: l.split(' '))
    instructions = [(DD[d], int(dist)) for d, dist, _ in raw]
    new_instructions = [(int(colour[-2]), int(colour[2:-2], 16))
                        for _, _, colour in raw]

    p1 = area(instructions)
    p2 = area(new_instructions)
    print(f'{p1=}')
    print(f'{p2=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '18.in'
    main(file)
