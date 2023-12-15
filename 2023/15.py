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

    p1 = sum(map(hash_, data))
    print(f'{p1=}')

    boxes = u.defaultdict(list)
    focal = {}
    for word in data:
        if word[-1] == '-':
            label = word[:-1]
            hash__ = hash_(label)
            if label in boxes[hash__]:
                boxes[hash__].remove(label)
        else:
            label, focus = word.split('=')
            focus = int(focus)
            hash__ = hash_(label)
            if label not in boxes[hash__]:
                boxes[hash__].append(label)
            focal[label] = focus

    p2 = 0
    for k, v in boxes.items():
        for i, label in enumerate(v):
            p2 += (k + 1) * (i + 1) * focal[label]
    print(f'{p2=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '15.in'
    main(file)
