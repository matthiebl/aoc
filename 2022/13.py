#!/usr/bin/env python3.12

import aocutils as u
from sys import argv
from functools import cmp_to_key


def balanced(left: list, right: list) -> int:
    for itl, itr in zip(left, right):
        if isinstance(itl, int) and isinstance(itr, int):
            if itl > itr:
                return -1
            if itl < itr:
                return 1
        elif isinstance(itl, list) and isinstance(itr, list):
            result = balanced(itl, itr)
            if result != 0:
                return result
        elif isinstance(itl, int):
            result = balanced([itl], itr)
            if result != 0:
                return result
        else:
            result = balanced(itl, [itr])
            if result != 0:
                return result

    if len(left) < len(right):
        return 1
    if len(right) < len(left):
        return -1
    return 0


def main(file: str) -> None:
    print('Day 13')

    pairs = u.input_from_grouped_lines(file, map=u.list_eval)
    # pairs = [[literal_eval(side) for side in pair.split('\n')]
    #  for pair in raw]

    p1 = 0
    for index, [left, right] in enumerate(pairs, start=1):
        if balanced(left, right) > 0:
            p1 += index
    print(f'{p1=}')

    packets = []
    for [left, right] in pairs:
        packets.append(left)
        packets.append(right)

    packets.append([[2]])
    packets.append([[6]])

    packets.sort(key=cmp_to_key(balanced), reverse=True)

    p2 = 1
    for index, packet in enumerate(packets, start=1):
        if packet == [[2]] or packet == [[6]]:
            p2 *= index
    print(f'{p2=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '13.in'
    main(file)
