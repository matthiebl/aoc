#!/usr/bin/env python3.10

from sys import argv
from collections import defaultdict
import aocutils as u


ALLOWED = {
    'red': 12,
    'green': 13,
    'blue': 14,
}


def main(file: str) -> None:
    print('Day 02')

    data = u.input_as_lines(file)

    p1 = 0
    p2 = 0
    for line in data:
        [game_info, game] = line.split(': ')
        id = int(game_info[5:])
        game = u.double_sep(game, '; ', ', ')

        min_needed = defaultdict(int)

        invalid = False
        for hand in game:
            for cube in hand:
                count, colour = cube.split(' ')
                count = int(count)

                if count > ALLOWED[colour]:
                    invalid = True
                min_needed[colour] = max(min_needed[colour], count)

        if not invalid:
            p1 += id

        p2 += min_needed['red'] * min_needed['green'] * min_needed['blue']

    print(f'{p1=}')
    print(f'{p2=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '02.in'
    main(file)
