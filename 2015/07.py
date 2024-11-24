#!/usr/bin/env python3.12

from sys import argv

import aocutils as u


def to_bin(n):
    if isinstance(n, str):
        return f'{bin(int(n))[2:]:0>16}'
    if isinstance(n, int):
        return f'{bin(n)[2:]:0>16}'
    raise Exception('to_bin input is invalid')


def from_bin(n: str):
    return int(n, 2)


def b_not(n: str):
    return ''.join(['1' if c == '0' else '0' for c in n])


def b_or(a: str, b: str):
    return ''.join(['1' if x == '1' or y == '1' else '0' for x, y in zip(a, b)])


def b_and(a: str, b: str):
    return ''.join(['1' if x == '1' and y == '1' else '0' for x, y in zip(a, b)])


def b_left(a: str, n: int):
    return a[n:] + '0' * n


def b_right(a: str, n: int):
    return '0' * n + a[:-n]


def main(file: str) -> None:
    print('Day 07')

    data = u.input_as_lines(file, map=str.split)
    circuit = {s: rs for [*rs, _, s] in data}

    signals = {}

    # @u.print_result
    def run(s):
        if s.isnumeric():
            return to_bin(s)
        if s in signals:
            return signals[s]
        rs = circuit[s]

        # print(s, rs)
        if len(rs) == 1:
            signals[s] = run(rs[0])
            return signals[s]

        if rs[0] == 'NOT':
            signals[s] = b_not(run(rs[1]))
        elif rs[1] == 'OR':
            signals[s] = b_or(run(rs[0]), run(rs[2]))
        elif rs[1] == 'AND':
            signals[s] = b_and(run(rs[0]), run(rs[2]))
        elif rs[1] == 'LSHIFT':
            signals[s] = b_left(run(rs[0]), int(rs[2]))
        elif rs[1] == 'RSHIFT':
            signals[s] = b_right(run(rs[0]), int(rs[2]))
        else:
            raise Exception('what is', s, rs)
        return signals[s]

    p1 = from_bin(run('a'))
    print(f'{p1=}')

    signals = {}
    signals['b'] = to_bin(p1)

    p2 = from_bin(run('a'))
    print(f'{p2=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '07.in'
    main(file)
