#!/usr/bin/env python3.10

from sys import argv
import advent as adv


def get_digit(line, i):
    if line[i] in '1234567890':
        return int(line[i])
    if line[i:i+3] == 'one':
        return 1
    if line[i:i+3] == 'two':
        return 2
    if line[i:i+5] == 'three':
        return 3
    if line[i:i+4] == 'four':
        return 4
    if line[i:i+4] == 'five':
        return 5
    if line[i:i+3] == 'six':
        return 6
    if line[i:i+5] == 'seven':
        return 7
    if line[i:i+5] == 'eight':
        return 8
    if line[i:i+4] == 'nine':
        return 9
    return None


def main(file: str) -> None:
    print('Day 01')

    data = adv.input_as_lines(file)

    p1 = 0
    for line in data:
        n1 = 0
        while line[n1] not in '1234567890':
            n1 += 1
        n2 = len(line) - 1
        while line[n2] not in '1234567890':
            n2 -= 1
        n = line[n1] + line[n2]
        p1 += int(n)
    print(f'{p1=}')

    p2 = 0
    for line in data:
        n1 = 0
        while get_digit(line, n1) == None:
            n1 += 1
        n2 = len(line) - 1
        while get_digit(line, n2) == None:
            n2 -= 1
        n = get_digit(line, n1) * 10 + get_digit(line, n2)
        p2 += n
    print(f'{p2=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '01.in'
    main(file)
