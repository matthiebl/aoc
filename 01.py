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


def get_first(line: str, pred):
    i = 0
    while pred(line, i) == None:
        i += 1
    return pred(line, i)


def get_last(line: str, pred):
    i = len(line) - 1
    while pred(line, i) == None:
        i -= 1
    return pred(line, i)


def main(file: str) -> None:
    print('Day 01')

    data = adv.input_as_lines(file)

    p1 = 0
    for line in data:
        line = list(filter(lambda x: x in '123456789', line))
        p1 += int(line[0]) * 10 + int(line[-1])
    print(f'{p1=}')

    p2 = 0
    for line in data:
        n1 = get_first(line, get_digit)
        n2 = get_last(line, get_digit)
        p2 += n1 * 10 + n2
    print(f'{p2=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '01.in'
    main(file)
