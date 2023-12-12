#!/usr/bin/env python3.12

import aocutils as u
from sys import argv
from collections import defaultdict


def main(file: str) -> None:
    print('Day 04')

    data = [line[8:].strip().split(' | ')
            for line in u.input_as_lines(file)]

    cards = defaultdict(int)
    p1 = 0
    for i, [winning, mine] in enumerate(data):
        winning = set(u.find_digits(winning))
        mine = set(u.find_digits(mine))

        matching_numbers = len(winning & mine)
        if matching_numbers > 0:
            p1 += 2 ** (matching_numbers - 1)

        cards[i + 1] += 1
        for j in range(matching_numbers):
            cards[i + j + 2] += cards[i + 1]

    p2 = sum(cards.values())
    print(f'{p1=}')
    print(f'{p2=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '04.in'
    main(file)
