#!/usr/bin/env python3.12

import aocutils as u
from sys import argv


def det_die() -> u.Iterable[int]:
    die = 0
    while True:
        yield (die + 1, (die % 100) + 1)
        die += 1


def det_dice(die) -> u.Iterable[int]:
    _, v1 = next(die)
    _, v2 = next(die)
    rolls, v3 = next(die)
    return rolls, v1 + v2 + v3


class Pawn:
    def __init__(self, pos: int) -> None:
        self.pos = pos
        self.score = 0

    def move(self, spaces: int) -> None:
        self.pos = (self.pos + spaces) % 10
        self.score += self.pos + 1

    def won(self) -> bool:
        return self.score >= 1000


def main(file: str) -> None:
    print('Day 21')

    [a, b] = u.input_as_lines(file, map=lambda s: u.find_digits(s)[1] - 1)
    pawn1 = Pawn(a)
    pawn2 = Pawn(b)
    die = det_die()

    p1 = 0
    while True:
        rolls, value = det_dice(die)
        pawn1.move(value)
        if pawn1.won():
            p1 = pawn2.score * rolls
            print('p1 won', pawn2.score, rolls)
            break

        rolls, value = det_dice(die)
        pawn2.move(value)
        if pawn2.won():
            p2 = pawn1.score * rolls
            print('p2 won', pawn1.score, rolls)
            break
    print(f'{p1=}')

    def play(pos1, pos2, score1, score2):
        


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '21.in'
    main(file)
