"""
--- Day 13: Mine Cart Madness ---
https://adventofcode.com/2018/day/13
"""

from utils import *

args = parse_args(year=2018, day=13)
raw = get_input(args.filename, year=2018, day=13)

grid = [list(line) for line in raw.splitlines()]
R, C = len(grid), len(grid[0])

moves = {"<": (0, -1), "^": (-1, 0), ">": (0, 1), "v": (1, 0)}
turns = {
    "<": ["v", "<", "^"],
    "^": ["<", "^", ">"],
    ">": ["^", ">", "v"],
    "v": [">", "v", "<"],
}
corners = {
    ("<", "/"): "v", ("<", "\\"): "^", ("<", "-"): "<",
    ("^", "/"): ">", ("^", "\\"): "<", ("^", "|"): "^",
    (">", "/"): "^", (">", "\\"): "v", (">", "-"): ">",
    ("v", "/"): "<", ("v", "\\"): ">", ("v", "|"): "v",
}

carts = []
for r, c in find_in_grid(grid, "<>^v"):
    carts.append((r, c, grid[r][c], 0))
    grid[r][c] = "-" if grid[r][c] in "<>" else "|"

p1 = None
while len(carts) > 1:
    updated_carts = {(r, c): None for r, c, _, _ in carts}
    for r, c, f, t in carts:
        if (r, c) not in updated_carts:
            continue
        del updated_carts[r, c]
        nr, nc = tuple_add((r, c), moves[f])
        if (nr, nc) in updated_carts:
            if p1 is None:
                p1 = f"{nc},{nr}"
            del updated_carts[nr, nc]
        elif grid[nr][nc] == "+":
            updated_carts[nr, nc] = (turns[f][t], (t + 1) % 3)
        else:
            updated_carts[nr, nc] = (corners[f, grid[nr][nc]], t)
    carts = sorted((r, c, f, t) for (r, c), (f, t) in updated_carts.items())

[(r, c, _, _)] = carts
p2 = f"{c},{r}"

print(p1)
print(p2)

if args.test:
    args.tester(p1, p2)
