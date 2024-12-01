#!/usr/bin/env python3.12

from itertools import permutations
from sys import argv

import aocutils as u


def main(file: str) -> None:
    print('Day 13')

    data = u.input_as_lines(file, map=str.split)

    people = set()
    happiness = u.defaultdict(int)

    for [name, _, change, amt, *_, next_to] in data:
        people.add(name)
        happiness[tuple(sorted([name, next_to[:-1]]))] += int(amt) * (1 if change == 'gain' else -1)

    people = sorted(people)

    p1 = 0
    for arrangement in permutations(people, len(people)):
        score = happiness[tuple(sorted([arrangement[0], arrangement[-1]]))]
        for name1, name2 in u.window(arrangement):
            score += happiness[tuple(sorted([name1, name2]))]
        p1 = max(p1, score)
    print(f'{p1=}')

    people.append('Me')
    p2 = 0
    for arrangement in permutations(people, len(people)):
        score = 0
        if arrangement[0] != 'Me' and arrangement[-1] != 'Me':
            score += happiness[tuple(sorted([arrangement[0], arrangement[-1]]))]
        for name1, name2 in u.window(arrangement):
            if name1 == 'Me' or name2 == 'Me':
                continue
            score += happiness[tuple(sorted([name1, name2]))]
        p2 = max(p2, score)
    print(f'{p2=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '13.in'
    main(file)
