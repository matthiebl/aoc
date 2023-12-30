#!/usr/bin/env python3.12

import aocutils as u
from sys import argv

h_to_b = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111',
}


class Packet:
    def __init__(self, **kwargs) -> None:
        self.data = kwargs
        self.sub: list[Packet] = []

    def sum(self, key: str):
        return self.data[key] + sum([p.sum(key) for p in self.sub])

    def value(self) -> int:
        match self.data['tid']:
            case 0:
                return sum(p.value() for p in self.sub)
            case 1:
                return u.mul(p.value() for p in self.sub)
            case 2:
                return min(p.value() for p in self.sub)
            case 3:
                return max(p.value() for p in self.sub)
            case 4:
                return self.data['n']
            case 5:
                return 1 if self.sub[0].value() > self.sub[1].value() else 0
            case 6:
                return 1 if self.sub[0].value() < self.sub[1].value() else 0
            case 7:
                return 1 if self.sub[0].value() == self.sub[1].value() else 0


def parse(s: str):
    version = int(s[:3], 2)
    tid = int(s[3:6], 2)
    sub = []
    p = Packet(v=version, tid=tid)

    plen = 6
    if tid == 4:
        n = ''
        while s[plen] == '1':
            n += s[plen + 1: plen + 5]
            plen += 5
        n += s[plen + 1: plen + 5]
        plen += 5

        p.data['n'] = int(n, 2)

    elif s[plen] == '0':
        L = int(s[plen + 1: plen + 16], 2)
        plen += 16
        splens = 0
        while splens < L:
            splen, sp = parse(s[plen:])
            plen += splen
            splens += splen
            sub.append(sp)
    else:
        L = int(s[plen + 1: plen + 12], 2)
        plen += 12
        for _ in range(L):
            splen, sp = parse(s[plen:])
            plen += splen
            sub.append(sp)

    p.sub = sub

    return plen, p


def main(file: str) -> None:
    print('Day 16')

    hexi = u.read_input(file)

    binary = ''.join([h_to_b[h] for h in hexi])

    _, p = parse(binary)

    p1 = p.sum('v')
    print(f'{p1=}')

    p2 = p.value()
    print(f'{p2=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '16.in'
    main(file)
