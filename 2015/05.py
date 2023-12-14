#!/usr/bin/env python3.12

import aocutils as u
from sys import argv


def nice(s: str) -> bool:
    if 'ab' in s or 'cd' in s or 'pq' in s or 'xy' in s:
        return False
    double = False
    for a, b in zip(s, s[1:]):
        if a == b:
            double = True
    freq = u.Counter(s)
    vowels = freq['a'] + freq['e'] + freq['i'] + freq['o'] + freq['u']
    return double and vowels >= 3


def nice2(s: str) -> bool:
    pred1 = False
    for i in range(len(s) - 1):
        t = s[i:i+2]
        if t in s[:i] or t in s[i+2:]:
            pred1 = True
    pred2 = False
    for a, b in zip(s, s[2:]):
        if a == b:
            pred2 = True
    return pred1 and pred2


def main(file: str) -> None:
    print('Day 5')

    data = u.input_as_lines(file)

    p1 = len(list(filter(nice, data)))
    print(f'{p1=}')

    p2 = len(list(filter(nice2, data)))
    print(f'{p2=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '05.in'
    main(file)
