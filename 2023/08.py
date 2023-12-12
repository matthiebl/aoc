#!/usr/bin/env python3.10

from sys import argv
import math
import advent as adv


def main(file: str) -> None:
    print('Day 08')

    [[instructions], graph] = adv.input_from_grouped_lines(file)

    G = {}
    for line in graph:
        o = line[:3]
        l = line[7:10]
        r = line[12:15]
        G[o] = (l, r)

    p1 = 0
    i = 0
    pos = 'AAA'
    while pos != 'ZZZ':
        dir = instructions[i]
        pos = G[pos][0] if dir == 'L' else G[pos][1]
        i = (i + 1) % len(instructions)
        p1 += 1
    print(f'{p1=}')

    pos = [p for p in G if p[-1] == 'A']
    takes = []
    for p in pos:
        t = 0
        i = 0
        while p[-1] != 'Z':
            dir = instructions[i]
            p = G[p][0] if dir == 'L' else G[p][1]
            i = (i + 1) % len(instructions)
            t += 1
        takes.append(t)

    p2 = math.lcm(*takes)
    print(f'{p2=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '08.in'
    main(file)
