#!/usr/bin/env python3.12

import aocutils as u
from sys import argv

from hashlib import md5


def coin(hash: str, zeroes=5) -> bool:
    return hash.startswith('0' * zeroes)


def main(file: str) -> None:
    print('Day 4')

    secret = u.read_input(file)

    p1 = 0
    while not coin(md5((secret + str(p1)).encode()).hexdigest()):
        p1 += 1
    print(f'{p1=}')

    p2 = 0
    while not coin(md5((secret + str(p2)).encode()).hexdigest(), zeroes=6):
        p2 += 1
    print(f'{p2=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '04.in'
    main(file)
