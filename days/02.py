#!/usr/bin/env python3.10

from sys import argv
import advent as adv


def main(file: str) -> None:
    print('Day 02')

    data = adv.input_as_lines(file)

    p1 = 0
    p2 = 0
    for line in data:
        [game_info, game] = line.split(': ')
        id = int(game_info[5:])
        game = adv.double_sep(game, '; ', ', ')

        red = 0
        green = 0
        blue = 0

        invalid = False
        for hand in game:
            for cube in hand:
                count, colour = cube.split(' ')
                count = int(count)
                if colour == 'red':
                    red = max(red, count)
                if colour == 'green':
                    green = max(green, count)
                if colour == 'blue':
                    blue = max(blue, count)

                if colour == 'red' and count > 12:
                    invalid = True
                elif colour == 'green' and count > 13:
                    invalid = True
                elif colour == 'blue' and count > 14:
                    invalid = True
        if not invalid:
            p1 += id
        p2 += red * blue * green

    print(f'{p1=}')
    print(f'{p2=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '02.in'
    main(file)
