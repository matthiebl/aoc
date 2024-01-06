#!/usr/bin/env python3.12

import aocutils as u
from sys import argv

EXTRA = 0


def main(file: str) -> None:
    print('Day 20')

    [[algorithm], raw_image] = u.input_from_grouped_lines(file)

    default = ['0']
    image = {}

    for y, row in enumerate(raw_image):
        for x, ch in enumerate(row):
            image[(x, y)] = '1' if ch == '#' else '0'

    def value(x, y):
        if (x, y) not in image:
            return default[0]
        return image[(x, y)]

    def enhance():
        mnx, mny, mxx, mxy = u.min_max_x_y(image)
        new_image = {}
        for x in range(mnx - 1 - EXTRA, mxx + 2 + EXTRA):
            for y in range(mny - 1 - EXTRA, mxy + 2 + EXTRA):
                index = ''
                for dy in [-1, 0, 1]:
                    for dx in [-1, 0, 1]:
                        index += value(x + dx, y + dy)
                new_image[(x, y)] = '1' if algorithm[int(index, 2)] == '#' else '0'
        default[0] = '1' if default[0] == '0' else '0'
        return new_image

    # u.visualise([(x, y) for x, y in image if image[(x, y)] == '1'])
    # image = enhance()
    # u.visualise([(x, y) for x, y in image if image[(x, y)] == '1'])
    # image = enhance()
    # u.visualise([(x, y) for x, y in image if image[(x, y)] == '1'])

    # p1 = len([ch for _, ch in image.items() if ch == '1'])

    p1 = 0
    for t in range(50):
        if t == 2:
            p1 = len([ch for _, ch in image.items() if ch == '1'])
        image = enhance()
    print(f'{p1=}')

    p2 = len([ch for _, ch in image.items() if ch == '1'])
    print(f'{p2=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '20.in'
    main(file)
