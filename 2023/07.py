#!/usr/bin/env python3.12

from sys import argv
import aocutils as u
from collections import Counter

card_val = {
    'A': 13,
    'K': 12,
    'Q': 11,
    'J': 10,
    'T': 9,
    '9': 8,
    '8': 7,
    '7': 6,
    '6': 5,
    '5': 4,
    '4': 3,
    '3': 2,
    '2': 1,
}

card_val_p2 = {
    'A': 13,
    'K': 12,
    'Q': 11,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2,
    'J': 1,
}


def eq(l):
    if len(l) == 0:
        return True
    s = l[0]
    for i in l:
        if i != s:
            return False
    return True


def none_eq(l):
    # assume l is sorted
    assert len(l) > 0
    last = l[0]
    for c in l[1:]:
        if last == c:
            return False
        last = c
    return True


def card_values(hand: str, lookup: dict[str, int]):
    val = 0
    for card in list(hand):
        val = val * 100 + lookup[card]
    return val


def value(hand: str) -> int:
    val = card_values(hand, card_val)
    freq = Counter(list(hand))
    type_ = 1
    if len(freq) == 1:
        type_ = 7  # five kind
    elif len(freq) == 2 and 4 in freq.values():
        type_ = 6  # four kind
    elif len(freq) == 2:
        type_ = 5  # full house
    elif 3 in freq.values():
        type_ = 4  # three kind
    elif len(freq) == 3:
        type_ = 3  # two pair
    elif len(freq) == 4:
        type_ = 2  # one pair
    return val + type_ * 10000000000


def value2(hand: str) -> int:
    val = card_values(hand, card_val_p2)
    jokerless = sorted([c for c in hand if c != 'J'])

    if len(jokerless) == len(hand):
        return value(hand) - card_values(hand, card_val) + val

    freq = Counter(jokerless)

    type_ = 2
    if len(freq) == 0 or len(freq) == 1:
        type_ = 7  # five kind
    elif len(freq) == 2 and 1 in freq.values():
        type_ = 6  # four
    elif len(freq) == 2:
        type_ = 5  # full house
    elif len(freq) == 3:
        type_ = 4  # three kind

    return val + type_ * 10000000000


def main(file: str) -> None:
    print('Day 07')

    hands = u.input_as_lines(file, map=lambda s: (
        s.split()[0], int(s.split()[1])))

    hands.sort(key=lambda t: value(t[0]))

    p1 = sum(bid * (rank + 1) for rank, (_, bid) in enumerate(hands))
    print(f'{p1=}')

    hands.sort(key=lambda t: value2(t[0]))

    p2 = sum(bid * (rank + 1) for rank, (_, bid) in enumerate(hands))
    print(f'{p2=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '07.in'
    main(file)
