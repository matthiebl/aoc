"""
--- Day 9: Marble Mania ---
https://adventofcode.com/2018/day/9
"""

from collections import defaultdict

from utils import *

args = parse_args(year=2018, day=9)
raw = get_input(args.filename, year=2018, day=9)

players, marbles = nums(raw)


def highest_score(player: int, marbles: int):
    scores = defaultdict(int)
    list = CircularList()
    list.insert(0)

    player = 0
    for marble in range(1, marbles + 1):
        player += 1
        if marble % 23 == 0:
            scores[player] += marble + list.pop(-7)
        else:
            list.insert(marble, 1)
        player %= players

    return max(scores.values())


p1 = highest_score(players, marbles)
print(p1)

p2 = highest_score(players, marbles * 100)
print(p2)

if args.test:
    args.tester(p1, p2)
