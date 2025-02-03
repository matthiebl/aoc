"""
--- Day 22: Sporifica Virus ---
https://adventofcode.com/2017/day/22
"""

from utils import *

args = parse_args(year=2017, day=22)
raw = get_input(args.filename, year=2017, day=22)

grid = [list(line) for line in raw.splitlines()]
R, C = len(grid), len(grid[0])
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

infected = set(find_in_grid(grid, "#"))
r, c, d = R // 2, C // 2, 0
p1 = 0
for t in range(10000):
    d = (d + (1 if (r, c) in infected else -1)) % len(dirs)
    if (r, c) in infected:
        infected.remove((r, c))
    else:
        infected.add((r, c))
        p1 += 1
    r, c = tuple_add((r, c), dirs[d])
print(p1)

states = {p: "infected" for p in find_in_grid(grid, "#")}
r, c, d = R // 2, C // 2, 0
p2 = 0
for t in range(10000000):
    state = states.get((r, c), "clean")
    if state == "clean":
        d -= 1
        states[(r, c)] = "weakened"
    elif state == "weakened":
        states[(r, c)] = "infected"
        p2 += 1
    elif state == "infected":
        d += 1
        states[(r, c)] = "flagged"
    elif state == "flagged":
        d += 2
        states[(r, c)] = "clean"
    d %= len(dirs)
    r, c = tuple_add((r, c), dirs[d])
print(p2)

if args.test:
    args.tester(p1, p2)
