"""
--- Day 15: Warehouse Woes ---
https://adventofcode.com/2024/day/15
"""

from utils import *

args = parse_args(year=2024, day=15)
raw = get_input(args.filename, year=2024, day=15)

lines = raw.splitlines()

raw_grid, moves = [group.strip() for group in raw.split("\n\n")]
moves = "".join(moves.split())

room = [list(line) for line in raw_grid.splitlines()]
R, C = len(room), len(room[0])

# Transform to doubly wide room
transform = {"@": "@.", "#": "##", "O": "[]", ".": ".."}
room_wide = [list("".join(transform[c] for c in row)) for row in room]

D = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}

rr, rc = next(find_in_grid(room, "@"))
for move in moves:
    dr, dc = D[move]
    nr, nc = rr + dr, rc + dc
    while room[nr][nc] == "O":
        nr, nc = nr + dr, nc + dc
    if room[nr][nc] == ".":
        room[rr][rc] = "."
        room[nr][nc] = "O"
        rr, rc = rr + dr, rc + dc
        room[rr][rc] = "@"

p1 = sum(100 * r + c for (r, c), val, _ in enumerate_grid(room) if val == "O")
print(p1)


def move_blocks(dr: int, dc: int, blocks: set) -> bool:
    new_blocks = []
    for r, c in blocks:
        nr, nc = r + dr, c + dc
        if room_wide[nr][nc] == "#":
            return False
        if room_wide[nr][nc] == "[":
            new_blocks += [(nr, nc), (nr, nc + 1)]
        elif room_wide[nr][nc] == "]":
            new_blocks += [(nr, nc), (nr, nc - 1)]
    new_blocks = set(new_blocks) - blocks
    if len(new_blocks) != 0 and not move_blocks(dr, dc, new_blocks):
        return False
    blocks = list(sorted(blocks))
    for r, c in (blocks[::-1] if dc == 1 else blocks):
        room_wide[r][c], room_wide[r + dr][c + dc] = room_wide[r + dr][c + dc], room_wide[r][c]
    return True


rr, rc = next(find_in_grid(room_wide, "@"))
for move in moves:
    dr, dc = D[move]
    nr, nc = tuple_add((rr, rc), (dr, dc))
    if (room_wide[nr][nc] == "."
                or (room_wide[nr][nc] == "[" and move_blocks(dr, dc, set([(nr, nc), (nr, nc + 1)])))
                or (room_wide[nr][nc] == "]" and move_blocks(dr, dc, set([(nr, nc), (nr, nc - 1)])))
            ):
        room_wide[nr][nc] = "@"
        room_wide[rr][rc] = "."
        rr, rc = nr, nc

p2 = sum(100 * r + c for (r, c), val, _ in enumerate_grid(room_wide) if val == "[")
print(p2)

if args.test:
    args.tester(p1, p2)
