#!/usr/bin/env python3.12

import aocutils as u
from sys import argv


class Packet:
    def __init__(self, **kwargs) -> None:
        self.data = kwargs
        self.sub = []


def main(file: str) -> None:
    print('Day 14')

    [[polymer], rules] = u.input_from_grouped_lines(file)

    pairs = {}
    produce = {}

    for a, b in zip(polymer, polymer[1:]):
        pairs[a + b] = pairs.get(a + b, 0) + 1

    for rule in rules:
        pair, a = rule.split(' -> ')
        produce[pair] = [pair[0] + a, a + pair[1]]

    def step():
        new_pairs = {}
        for pair, amt in pairs.items():
            if pair in produce:
                a, b = produce[pair]
                new_pairs[a] = new_pairs.get(a, 0) + amt
                new_pairs[b] = new_pairs.get(b, 0) + amt
            else:
                new_pairs[pair] = new_pairs.get(pair, 0) + amt
        return new_pairs

    def score():
        freq = {}
        for pair, amt in pairs.items():
            a = pair[0]
            freq[a] = freq.get(a, 0) + amt
        a = polymer[-1]
        freq[a] = freq.get(a, 0) + 1

        lst = sorted([(v, k) for k, v in freq.items()])
        return lst[-1][0] - lst[0][0]

    for _ in range(10):
        pairs = step()

    p1 = score()
    print(f'{p1=}')

    for _ in range(30):
        pairs = step()

    p2 = score()
    print(f'{p2=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '14.in'
    main(file)
