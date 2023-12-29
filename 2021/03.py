#!/usr/bin/env python3.12

import aocutils as u
from sys import argv


def reduce(lst: list[str], default: str, prefix: str = '', depth: int = 0) -> str:
    if len(lst) == 1:
        return lst[0]

    (m, mc), (l, lc) = u.Counter(u.columns(lst)[depth]).most_common()
    prefix += (default if mc == lc else (m if default == '1' else l))

    return reduce([num for num in lst if num.startswith(prefix)], default, prefix, depth + 1)


def main(file: str) -> None:
    print('Day 03')

    diagnositc = u.input_as_lines(file)

    gamma = ''
    epsilon = ''
    for column in u.columns(diagnositc):
        (g, _), (e, _) = u.Counter(column).most_common()
        gamma += g
        epsilon += e

    p1 = int(gamma, 2) * int(epsilon, 2)
    print(f'{p1=}')

    oxygen = reduce(diagnositc, '1')
    carbon = reduce(diagnositc, '0')

    p2 = int(oxygen, 2) * int(carbon, 2)
    print(f'{p2=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '03.in'
    main(file)
