#!/usr/bin/env python3.12

import aocutils as u
from sys import argv
from functools import cache


@cache
def make_options(mask: str, length: int, nums: tuple[int]):
    if len(nums) == 0:
        if mask.count('#') == 0:
            return 1
        return 0

    first = nums[0]
    rest = nums[1:]
    to_leave = sum(rest) + len(rest)

    total = 0
    for dots in range(length - to_leave - first + 1):
        s = '.' * dots + '#' * first + '.'
        if not valid(mask, s):
            continue
        total += make_options(mask[len(s):], length - dots - first - 1, rest)

    return total


def valid(mask: str, opt: str) -> bool:
    return all(m == o or m == '?' for m, o in zip(mask, opt))


def main(file: str) -> None:
    print('Day 12')

    data = u.input_as_lines(file, map=lambda s: u.double_sep(s, ' ', ','))

    p1 = 0
    for [[line], nums] in data:
        nums = u.map_int(nums)
        p1 += make_options(line, len(line), tuple(nums))
    print(f'{p1=}')

    p2 = 0
    for [[line], nums] in data:
        nums = u.map_int(nums) * 5
        line = '?'.join([line] * 5)

        p2 += make_options(line, len(line), tuple(nums))
    print(f'{p2=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '12.in'
    main(file)
