"""
--- Day 20: Race Condition ---
https://adventofcode.com/2024/day/20
"""

from utils import *

args = parse_args(year=2024, day=20)
raw = get_input(args.filename, year=2024, day=20)

grid = [list(line) for line in raw.splitlines()]
R, C = len(grid), len(grid[0])

start = next(find_in_grid(grid, "S"))
end = next(find_in_grid(grid, "E"))

graph = grid_to_graph(grid, valid_tiles=".SE")
_, dists_from_end = dijkstras(graph, end, lambda x: False)
standard_time, dists_from_start = dijkstras(graph, start, is_end_pos(*end))

p1, p2 = 0, 0

for (r1, c1), v1, _ in enumerate_grid(grid, skip="#"):
    # Rather than search every other point in the grid to compare to
    # just limit to searching within the known limit we can cheat to
    for dr in range(-20, 21):
        for dc in range(-20, 21):
            r2, c2 = r1 + dr, c1 + dc
            if not within_grid(grid, r2, c2) or grid[r2][c2] == "#":
                continue
            man_dist = manhattan(r1, c1, r2, c2)
            skip_time = dists_from_start[(r1, c1)] + dists_from_end[(r2, c2)] + man_dist - 1
            if man_dist <= 2 and standard_time - skip_time >= 100:
                p1 += 1
            if man_dist <= 20 and standard_time - skip_time >= 100:
                p2 += 1

print(p1)
print(p2)

if args.test:
    args.tester(p1, p2)
