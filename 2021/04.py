"""
--- Day 4: Giant Squid ---
https://adventofcode.com/2021/day/4
"""

import numpy as np

from utils import *

args = parse_args(year=2021, day=4)
raw = get_input(args.filename, year=2021, day=4)

[[called], *boards] = [group.splitlines() for group in raw.split("\n\n")]
called = list(nums(called))

boards = [np.array([list(nums(row)) for row in board]) for board in boards]

scores = []
for call in called:
    for board in boards:
        board[board == call] = -1
    next_boards = []
    for board in boards:
        if any(np.sum(board, axis=0) == -5) or any(np.sum(board, axis=1) == -5):
            scores.append(np.sum((board != -1) * board) * call)
        else:
            next_boards.append(board)
    boards = next_boards

p1 = scores[0]
print(p1)

p2 = scores[-1]
print(p2)

if args.test:
    args.tester(p1, p2)
