"""
--- Day 12: Garden Groups ---

https://adventofcode.com/2024/day/12

Another problem that isn't straightforward to solve. The general solution I have taken is as follows.

To determine the garden plots, we use a BFS to search the grid until we reach a different type of
plant. We can determine the entire plot though the collection of same plants within the search. The
area will then be the length of this set, and the perimeter is the number of times we cross out of
bounds or to another type of plant. Every time we find a cell that is part of a plot, it is marked
as visited, so the same plot is not searched twice.

Then to determine the number of sides, we reach a more difficult problem. It isn't too obvious how we
could directly find the sides themselves, but for 2D shapes (other than a circle), the number of
sides will be equal to the number of corners.

With this in mind, we just need to check each of the 3 cases (* corner, # in plot, . out of plot):

Concave corner:
```
####
#*##
##..
##..
```

Convex corner:
```
##..
#*..
....
....
```

Interior corner:
```
####
#*.#
#.##
####
```

If we check every plant of the plot for each of these cases, in all 4 orientations, we should get the
total number of corners of the plot. This gives us the number of sides, which we use to get part b.
"""

from collections import deque
from utils import *

args = parse_args(year=2024, day=12)
raw = get_input(args["filename"], year=2024, day=12)

grid = [list(line) for line in raw.splitlines()]
R, C = len(grid), len(grid[0])

graph = grid_to_graph(grid)

p1 = 0
plots = []
visited = set()
for (r, c), v, _ in enumerate_grid(grid):
    if (r, c) in visited:
        continue

    perim = 0
    plot = set()
    queue = deque([(0, (r, c))])
    while queue:
        _, nxt = queue.popleft()

        rr, cc = nxt
        if grid[rr][cc] != v:
            perim += 1
            continue

        if nxt in visited:
            continue
        visited.add(nxt)
        plot.add(nxt)

        for dr, dc in directions():
            if not within_grid(grid, rr + dr, cc + dc):
                perim += 1
        
        queue.extend(list(graph[nxt]))

    p1 += len(plot) * perim
    plots.append(plot)

print(p1)

corner_checks  = [
    directions([1, 2, 5]),
    directions([5, 8, 7]),
    directions([7, 6, 3]),
    directions([3, 0, 1]),
]


def in_plot(plot, r, c):
    if not within_grid(grid, r, c):
        return False
    return (r, c) in plot


def is_corner(plot, adj):
    [(r1, c1), (r2, c2), (r3, c3)] = adj
    return ((in_plot(plot, r1, c1)) and (not in_plot(plot, r2, c2)) and (in_plot(plot, r3, c3))
            or (not in_plot(plot, r1, c1)) and (not in_plot(plot, r3, c3)))


p2 = 0
for plot in plots:
    corners = 0
    for r, c in plot:
        adj = [[tuple_add((r, c), t) for t in corner] for corner in corner_checks]
        corners += sum(1 for corner in adj if is_corner(plot, corner))
    p2 += len(plot) * corners

print(p2)

assert p1 == 1421958
assert p2 == 885394
