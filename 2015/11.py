#!/usr/bin/env python3.12

from sys import argv

import aocutils as u


def next_pw(pw: str) -> str:
    last = pw[-1]
    if last == 'z':
        return next_pw(pw[:-1]) + 'a'
    return pw[:-1] + chr(ord(last) + 1)


def main(file: str) -> None:
    print('Day 11')

    seqs = [''.join(x) for x in u.window('abcdefghijklmnopqrstuvwxyz', 3)]

    def rule_straight(pw: str) -> bool:
        for s in seqs:
            if s in pw:
                return True
        return False

    def rule_iol(pw: str) -> bool:
        return not ('i' in pw or 'o' in pw or 'l' in pw)

    def rule_double(pw: str) -> bool:
        remainings = []
        for i in range(len(pw) - 1):
            if pw[i] == pw[i + 1]:
                remainings.append(pw[:i] + '_' + pw[i + 2:])
        for pw in remainings:
            for i in range(len(pw) - 1):
                if pw[i] == pw[i + 1]:
                    return True
        return False

    pw = u.read_input(file)
    print(next_pw(pw))

    p1 = None
    p2 = None
    while True:
        pw = next_pw(pw)
        if rule_straight(pw) and rule_iol(pw) and rule_double(pw):
            if p1:
                p2 = pw
                break
            p1 = pw
            print(f'{p1=}')
    print(f'{p2=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '11.in'
    main(file)
