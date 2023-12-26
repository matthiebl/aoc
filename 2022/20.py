#!/usr/bin/env python3.12

import aocutils as u
from sys import argv


def find(index, data):
    for i, (j, _) in enumerate(data):
        if index == j:
            return i


def mix(data: list[int]) -> None:
    for i in range(len(data)):
        index = find(i, data)
        j, val = data.pop(index)

        new_index = (index + val) % len(data)
        if new_index == 0 and index != 0:
            new_index = len(data)

        data.insert(new_index, (j, val))


def main(file: str) -> None:
    print('Day 20')

    data = list(enumerate(u.input_as_lines(file, map=int)))
    mix(data)
    data = [val for _, val in data]

    p1 = 0
    i = data.index(0) + 1
    for j in range(1, 3001):
        i %= len(data)
        if j in [1000, 2000, 3000]:
            p1 += data[i]
        i += 1
    print(f'{p1=}')

    data = [(i, val * 811589153)
            for i, val in enumerate(u.input_as_lines(file, map=int))]
    for _ in range(10):
        mix(data)
    data = [val for _, val in data]

    p2 = 0
    i = data.index(0) + 1
    for j in range(1, 3001):
        i %= len(data)
        if j in [1000, 2000, 3000]:
            p2 += data[i]
        i += 1
    print(f'{p2=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '20.in'
    main(file)
