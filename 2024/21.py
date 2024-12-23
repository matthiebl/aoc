"""
--- Day 21: Keypad Conundrum ---
https://adventofcode.com/2024/day/21
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
    p1 += int(code[:3]) * (shortest_length(code, 2))
    p2 += int(code[:3]) * (shortest_length(code, 25))
print(p1)
print(p2)

if args.test:
    args.tester(p1, p2)
