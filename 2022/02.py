#!/usr/bin/env python3.12

import aocutils as u
from sys import argv

WIN = 6
DRAW = 3
LOSE = 0

ROCK, X = 'A', 1
PAPER, Y = 'B', 2
SCISSORS, Z = 'C', 3

results1 = {
    (ROCK, 'X'): DRAW + X,
    (ROCK, 'Y'): WIN + Y,
    (ROCK, 'Z'): LOSE + Z,
    (PAPER, 'X'): LOSE + X,
    (PAPER, 'Y'): DRAW + Y,
    (PAPER, 'Z'): WIN + Z,
    (SCISSORS, 'X'): WIN + X,
    (SCISSORS, 'Y'): LOSE + Y,
    (SCISSORS, 'Z'): DRAW + Z,
}

results2 = {
    (ROCK, 'X'): LOSE + Z,
    (ROCK, 'Y'): DRAW + X,
    (ROCK, 'Z'): WIN + Y,
    (PAPER, 'X'): LOSE + X,
    (PAPER, 'Y'): DRAW + Y,
    (PAPER, 'Z'): WIN + Z,
    (SCISSORS, 'X'): LOSE + Y,
    (SCISSORS, 'Y'): DRAW + Z,
    (SCISSORS, 'Z'): WIN + X,
}


def main(file: str) -> None:
    print('Day 02')

    plays = u.input_as_lines(file, map=lambda s: (s[0], s[2]))

    p1 = sum(results1[play] for play in plays)
    print(f'{p1=}')

    p2 = sum(results2[play] for play in plays)
    print(f'{p2=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '02.in'
    main(file)
