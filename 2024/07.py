#!/usr/bin/env python3.12

import aocutils as u
from sys import argv


def combine(target: int, ns: list[int], curr: int, p2=False):
    if not ns and curr == target:
        return target
    if not ns or curr > target:
        return -1

    cp = ns.copy()
    n = cp.pop(0)
    if combine(target, cp, curr + n, p2) > 0:
        return target
    if combine(target, cp, curr * n, p2) > 0:
        return target
    if p2 and combine(target, cp, int(str(curr) + str(n)), p2) > 0:
        return target
    return -1


def main(file: str) -> None:
    print('Day 07')

    data = [u.find_digits(line) for line in u.input_as_lines(file)]

    p1 = sum(filter(lambda r: r > 0, (combine(res, ns[1:], ns[0]) for [res, *ns] in data)))
    print(f'{p1=}')

    p2 = sum(filter(lambda r: r > 0, (combine(res, ns[1:], ns[0], p2=True) for [res, *ns] in data)))
    print(f'{p2=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '07.in'
    main(file)
