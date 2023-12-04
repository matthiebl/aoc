#!/usr/bin/env python3.10

from sys import argv
import re
from collections import defaultdict
import advent as adv


def main(file: str) -> None:
    print('Day 04')

    data = [line[8:].strip().split(' | ')
            for line in adv.input_as_lines(file)]

    cards = defaultdict(int)
    p1 = 0
    for i, [winning, mine] in enumerate(data):
        winning = re.findall('\d+', winning)
        mine = re.findall('\d+', mine)

        matching_numbers = 0
        score = 0
        for n in winning:
            if n in mine:
                score = score * 2 if score > 0 else 1
                matching_numbers += 1
        p1 += score
        cards[i + 1] += 1
        for j in range(matching_numbers):
            cards[i + j + 2] += cards[i + 1]
    print(f'{p1=}')

    p2 = sum(cards.values())
    print(f'{p2=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '04.in'
    main(file)
