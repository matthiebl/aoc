"""
--- Day 7: Camel Cards ---
https://adventofcode.com/2023/day/7
"""

from collections import Counter
from functools import cmp_to_key
from utils import *

args = parse_args(year=2023, day=7)
raw = get_input(args.filename, year=2023, day=7)

cards = list(map(lambda t: tuple(t.split()), raw.splitlines()))

hand_type_value = {
    (5,): 60000000,
    (4, 1): 50000000,
    (3, 2): 40000000,
    (3, 1, 1): 30000000,
    (2, 2, 1): 20000000,
    (2, 1, 1, 1): 10000000,
    (1, 1, 1, 1, 1): 0,
}


def hand_type(hand):
    count = tuple(sorted(Counter(hand).values(), reverse=True))
    return hand_type_value[count]


def value(hand: str, jokers: bool = False):
    value = 0
    for c in hand:
        value = 15 * (value + ("J23456789TQKA" if jokers else "23456789TJQKA").index(c))
    if jokers:
        return max(value + hand_type(hand.replace("J", r)) for r in "23456789TQKA")
    return value + hand_type(hand)


cards.sort(key=lambda play: value(play[0]))
p1 = sum(i * int(bid) for i, (_, bid) in enumerate(cards, 1))
print(p1)

cards.sort(key=lambda play: value(play[0], jokers=True))
p2 = sum(i * int(bid) for i, (_, bid) in enumerate(cards, 1))
print(p2)

if args.test:
    args.tester(p1, p2)
