"""
--- Day 15: Warehouse Woes ---
https://adventofcode.com/2024/day/15
"""

from utils import *

args = parse_args(year=2024, day=15)
raw = get_input(args["filename"], year=2024, day=15)

lines = raw.splitlines()

grid, moves = [group.strip() for group in raw.split("\n\n")]
moves = moves.strip()

grid = [list(line) for line in grid.splitlines()]
R, C = len(grid), len(grid[0])


grid_2 = []
for row in grid:
    row_2 = ""
    for c in row:
        if c == "@":
            row_2 += "@."
        elif c == "#":
            row_2 += "##"
        elif c == ".":
            row_2 += ".."
        else:
            row_2 += "[]"
    grid_2.append(list(row_2))


def pg(g):
    for r in g:
        print("".join(r))


rr, rc = 0, 0
for (r, c), val, _ in enumerate_grid(grid):
    if val == "@":
        rr, rc = (r, c)
        break

D = {
    "^": (-1, 0),
    ">": (0, 1),
    "v": (1, 0),
    "<": (0, -1),
}

for move in moves:
    if move == "\n":
        continue
    dr, dc = D[move]
    nr, nc = tuple_add((rr, rc), (dr, dc))
    lr, lc = nr, nc
    while grid[lr][lc] == "O":
        lr, lc = tuple_add((lr, lc), (dr, dc))
    if grid[lr][lc] == "#":
        continue
    if grid[lr][lc] == ".":
        grid[lr][lc] = "O"
        grid[rr][rc] = "."
        grid[nr][nc] = "@"
        rr, rc = nr, nc

p1 = 0
for (r, c), val, _ in enumerate_grid(grid):
    if val == "O":
        p1 += 100 * r + c
print(p1)


def move_vert(dr, dc, blocks) -> bool:
    new_blocks = []
    for r, c in blocks:
        nr, nc = tuple_add((r, c), (dr, dc))
        if grid_2[nr][nc] == "#":
            return False
        if grid_2[nr][nc] == "[":
            new_blocks += [(nr, nc), (nr, nc + 1)]
        elif grid_2[nr][nc] == "]":
            new_blocks += [(nr, nc), (nr, nc - 1)]
    if len(new_blocks) == 0:
        for r, c in blocks:
            nr, nc = tuple_add((r, c), (dr, dc))
            grid_2[nr][nc] = grid_2[r][c]
            grid_2[r][c] = "."
        return True
    if not move_vert(dr, dc, list(set(new_blocks))):
        return False
    for r, c in blocks:
        nr, nc = tuple_add((r, c), (dr, dc))
        grid_2[nr][nc] = grid_2[r][c]
        grid_2[r][c] = "."
    return True


rr, rc = 0, 0
for (r, c), val, _ in enumerate_grid(grid_2):
    if val == "@":
        rr, rc = (r, c)
        break

for move in moves:
    if move == "\n":
        continue
    dr, dc = D[move]
    nr, nc = tuple_add((rr, rc), (dr, dc))
    if grid_2[nr][nc] == ".":
        grid_2[nr][nc] = "@"
        grid_2[rr][rc] = "."
        rr, rc = nr, nc
        continue
    if grid_2[nr][nc] == "#":
        continue
    if move in "^v":
        if (grid_2[nr][nc] == "[" and move_vert(dr, dc, [(nr, nc), (nr, nc + 1)])) or (grid_2[nr][nc] == "]" and move_vert(dr, dc, [(nr, nc), (nr, nc - 1)])):
            grid_2[nr][nc] = "@"
            grid_2[rr][rc] = "."
            rr, rc = nr, nc
    else:
        lr, lc = nr, nc
        while grid_2[lr][lc] in "[]":
            lr, lc = tuple_add((lr, lc), (dr, dc))
        if grid_2[lr][lc] == ".":
            if move == ">":
                grid_2[lr][rc+1:lc+1] = grid_2[lr][rc:lc]
                grid_2[rr][rc] = "."
            else:
                grid_2[lr][lc:rc] = grid_2[lr][lc+1:rc+1]
                grid_2[rr][rc] = "."
            rr, rc = nr, nc

p2 = 0
for (r, c), val, _ in enumerate_grid(grid_2):
    if val == "[":
        p2 += 100 * r + c
print(p2)

assert p1 == 1527563
assert p2 == 1521635
