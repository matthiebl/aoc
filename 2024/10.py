from collections import defaultdict
from utils import *

args = parse_args(year=2024, day=10)
raw = get_input(args["filename"], year=2024, day=10)

grid = [list(line) for line in raw.splitlines()]
R, C = len(grid), len(grid[0])

trail_heads = [(r, c) for r, row in enumerate(grid) for c, ch in enumerate(row) if ch == "0"]
trail_ends = defaultdict(set)


def trail_head_score(start, pos) -> int:
    r, c = pos
    ch = int(grid[r][c])
    if ch == 9:
        trail_ends[start].add(pos)
        return 1
    score = 0
    for dr, dc in directions():
        nr, nc = r + dr, c + dc
        if within_grid(grid, nr, nc) and int(grid[nr][nc]) == ch + 1:
            score += trail_head_score(start, (nr, nc))
    return score


p2 = 0
for pos in trail_heads:
    p2 += trail_head_score(pos, pos)
p1 = sum(len(s) for s in trail_ends.values())
print(p1)
print(p2)
