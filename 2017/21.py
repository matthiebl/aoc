"""
--- Day 21: Fractal Art ---
https://adventofcode.com/2017/day/21
"""

from utils import *

args = parse_args(year=2017, day=21)
raw = get_input(args.filename, year=2017, day=21)

translation = {}
for rule in raw.splitlines():
    from_, to_ = rule.split(" => ")
    from_ = from_.split("/")
    for _ in range(4):
        translation["/".join(from_)] = to_
        translation["/".join(from_[::-1])] = to_
        from_ = ["".join(x) for x in zip(*from_[::-1])]

grid = [
    list(".#."),
    list("..#"),
    list("###"),
]


def iteration(n: int):
    if n == 0:
        return sum(r.count("#") for r in grid)
    size = len(grid)
    new_grid = []
    step = 2 if size % 2 == 0 else 3
    for r in range(0, size, step):
        row = ["" for _ in range(3 if step == 2 else 4)]
        for c in range(0, size, step):
            chunk = "/".join("".join(chunk) for chunk in chunks([grid[rr][cc] for rr in range(r, r + step)
                                                                 for cc in range(c, c + step)], n=step))
            t = translation[chunk]
            for i, rr in enumerate(t.split("/")):
                row[i] += rr
        new_grid += row
    grid[:] = new_grid
    return iteration(n - 1)


p1 = iteration(5)
print(p1)

p2 = iteration(18 - 5)
print(p2)

if args.test:
    args.tester(p1, p2)
