#!/usr/bin/env python3.12

import aocutils as u
from sys import argv

"""
--- Day 21: Step Counter ---

This one was very interesting, and the solve for it was annoying
yet satisfying. Always look at your input when all seems lost...

First of all the key notices for part 2 were:
 - obviously, in a 2D grid, walking out makes a diamond
 - in the input (131 x 131), we can see that the start is
   directly in the middle, 65 steps from every edge
 - additionally, the input has a diamond shape gap where
   there are no walls, meaning after ~65 steps, the edges of
   the diamond we explore will be perfect edges
 - so, since the input repeats, we will eventually end up at
   consistent gaps at 65, 65 + 131, 65 + 131 + 131 steps, etc.

Hence, my approach is to expand out iteratively a few times,
(from this 65, 65 + 131, 65 + 262, 65 + 393, ...)
and see how many positions I can be in. Then, I expect this to
increase the same way we say increases in day 9's expansion
logic. So I can just keep expanding with that logic instead of
doing the hard work of the actual walks.
"""


TARGET_STEPS = 26501365


def find(field, f):
    for y, row in enumerate(field):
        for x, c in enumerate(row):
            if c == f:
                return (x, y)


def day9_expand(line):
    history: list[list[int]] = [line]
    while not all(n == 0 for n in history[-1]):
        new = []
        last = history[-1]
        for a, b in zip(last, last[1:]):
            new.append(b - a)
        history.append(new)
    history.reverse()
    history[0].append(0)
    for la, lb in zip(history, history[1:]):
        lb.append(lb[-1] + la[-1])
    history.reverse()


POS = set()


def main(file: str) -> None:
    print('Day 21')

    field = u.input_as_lines(file)

    POS.add(find(field, 'S'))

    def step(steps):
        if steps == 0:
            return
        new = set()
        for x, y in POS:
            for dx, dy in u.DXY:
                nx, ny = x + dx, y + dy
                if field[ny % 131][nx % 131] in '.S':
                    new.add((nx, ny))
        POS.clear()
        for n in new:
            POS.add(n)
        step(steps - 1)

    step(64)
    p1 = len(POS)
    print(f'{p1=}')

    step(1)  # Get to 65 steps (which is 131 // 2)
    scores = [len(POS)]
    for _ in range(2):
        step(131)  # Do two rounds of another 131 steps
        scores.append(len(POS))

    # Now use day 9 code to expand the next values
    for _ in range(TARGET_STEPS // 131 - 2):
        day9_expand(scores)
        scores = scores[-3:]
    p2 = scores[-1]
    print(f'{p2=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '21.in'
    main(file)
