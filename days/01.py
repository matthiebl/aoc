#!/usr/bin/env python3.10

from sys import argv
import advent as adv


def starts_with_index(s: str, l: list[str]) -> int:
    for i, match in enumerate(l):
        if s.startswith(match):
            return i
    return None


def get_digit(line: str, i: int) -> int:
    if line[i] in '1234567890':
        return int(line[i])
    return starts_with_index(line[i:i+5], ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'])


def first_first(line: str, start: int, inc: int, f):
    i = start
    while f(line, i) == None:
        i += inc
    return f(line, i)


def get_left_most(line: str, f):
    return first_first(line, 0, 1, f)


def get_right_most(line: str, f):
    return first_first(line, len(line) - 1, -1, f)


def main(file: str) -> None:
    print('Day 01')

    data = adv.input_as_lines(file)

    def first_last_dig(l):
        line = list(map(int, filter(lambda x: x in '123456789', l)))
        return line[0] * 10 + line[-1]
    p1 = sum(first_last_dig(line) for line in data)
    print(f'{p1=}')

    p2 = sum(get_left_most(line, get_digit) * 10 +
             get_right_most(line, get_digit) for line in data)
    print(f'{p2=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '01.in'
    main(file)
