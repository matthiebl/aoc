"""
--- Day 21: Keypad Conundrum ---
https://adventofcode.com/2024/day/21

This is the hardest problem I think we have faced so far. And likely the hardest of the year.

The problem is somewhat straight forward, for each code, find the corresponding path for the robot needed to move
around and press buttons. Then pass that path as the code to the next robot. However, we can be fairly certain that
the path is going to grow rapidly the more robots there are, which makes this iterative robot, by robot approach
infeasible.

Instead, we need to realise a few key points:

- It is never going to be better to make more moves than necessary between two buttons, as this will always cause
  strictly more moves for the next robot.
- All paths implicitly start at A, and hence every pair of buttons will cause the next robot to move from the "A",
  to the desired directional buttons in the path along the pair of buttons, back to the "A" to "press" the button.
- Each pair of buttons are independent due to the above point, so we do not need to work out the whole path of the
  next robot at once, just each pair of buttons.
- And finally, we only care about the length of the shortest path after `n` robots, and so never need to know what
  an entire path is at any point.

With this in mind, we can take a depth first approach, where we work out the minimum length of just the first move for
a robot recursively until the last robot, before moving to the next move. This way we are more likely to see the same
short segment of the path at each robot depth, and therefor cache the results.

I have implemented a specialised BFS that only tries to move in the direction of the target, and builds all the paths
between two points. I can use this to work out every path between two moves, and pass this path/code to my recursive
shortest path function.
"""

from collections import deque
from functools import cache
from utils import *

args = parse_args(year=2024, day=21)
raw = get_input(args.filename, year=2024, day=21)

codes = raw.splitlines()

numpad = (
    "789",
    "456",
    "123",
    ".0A",
)

keypad = (
    ".^A",
    "<v>",
)


@cache
def find_paths(pad: tuple[str], start: str, end: str):
    if start == end:
        return "A"
    (sr, sc), (er, ec) = next(find_in_grid(pad, start)), next(find_in_grid(pad, end))
    dr = 0 if er == sr else -1 if er < sr else 1
    dc = 0 if ec == sc else -1 if ec < sc else 1
    paths = []
    queue = deque([("", (sr, sc))])
    while queue:
        path, (r, c) = queue.popleft()
        if pad[r][c] == ".":
            continue
        if (r, c) == (er, ec):
            paths.append(path + "A")
            continue
        if r != er:
            queue.append((path + ("^" if dr < 0 else "v"), (r + dr, c)))
        if c != ec:
            queue.append((path + ("<" if dc < 0 else ">"), (r, c + dc)))
    return paths


@cache
def shortest_length(moves: str, steps: int, initial: bool = True):
    length = 0
    for a, b in windows("A" + moves):
        paths = find_paths(numpad if initial else keypad, a, b)
        if steps == 0:
            length += len(paths[0])
        else:
            length += min(shortest_length(path, steps - 1, False) for path in paths)
    return length


p1, p2 = 0, 0
for code in codes:
    p1 += int(code[:3]) * shortest_length(code, 2)
    p2 += int(code[:3]) * shortest_length(code, 25)
print(p1)
print(p2)

if args.test:
    args.tester(p1, p2)
