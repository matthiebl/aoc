#!/usr/bin/env python3.12

import aocutils as u
from sys import argv


def hash_(s):
    i = 0
    for c in s:
        i = ((i + ord(c)) * 17) % 256
    return i


def main(file: str) -> None:
    print('Day 15')

    data = u.read_input(file).split(',')

    p1 = 0
    for word in data:
        p1 += hash_(word)

    HASHMAP = {}
    for word in data:
        dash, eq = False, 0
        if word[-1] == '-':
            label = word[:-1]
            dash = True
        else:
            label = word[:-2]
            eq = int(word[-1])

        if dash:
            lens = HASHMAP.get(hash_(label), None)
            if lens is None:
                continue
            HASHMAP[hash_(label)] = list(filter(lambda t: t[0] != label, lens))
        else:
            lens = HASHMAP.get(hash_(label), None)
            if lens is None:
                HASHMAP[hash_(label)] = [(label, eq)]
                continue

            if len(list(filter(lambda t: t[0] == label, lens))) == 0:
                HASHMAP[hash_(label)].append((label, eq))
            else:
                HASHMAP[hash_(label)] = list(
                    map(lambda t: (t[0], eq if t[0] == label else t[1]), lens))

    print(f'{p1=}')

    p2 = 0
    for k, v in HASHMAP.items():
        for i, (label, focus) in enumerate(v):
            p2 += (k + 1) * (i + 1) * focus
    print(f'{p2=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '15.in'
    main(file)
