#!/usr/bin/env python3.12

import aocutils as u
from sys import argv

turn_left = {
    '>': '^',
    '^': '<',
    '<': 'v',
    'v': '>'
}

turn_right = {
    '>': 'v',
    '^': '>',
    '<': '^',
    'v': '<'
}

facing_score = {
    '>': 0,
    'v': 1,
    '<': 2,
    '^': 3
}


def main(file: str) -> None:
    print('Day 22')

    map, moves = u.input_from_grouped_lines(file)
    moves = moves.pop()

    SIZE = 50 if file == '22.in' else 4
    HEIGHT = len(map)
    WIDTH = max(len(r) for r in map)

    for i, r in enumerate(map):
        map[i] = r + ' ' * (WIDTH - len(r))

    pos = [0, 0]
    for i, c in enumerate(map[0]):
        if c == '.':
            pos = [i, 0]
            break
    pos2 = pos.copy()
    facing = '>'

    def move_right(pos):
        x, y = pos
        if x == WIDTH - 1 or map[y][x + 1] == ' ':
            for xx, c in enumerate(map[y]):
                if c == '#':
                    return False
                if c == '.':
                    pos[:] = [xx, y]
                    return True
        if map[y][x + 1] == '#':
            return False
        if map[y][x + 1] == '.':
            pos[:] = [x + 1, y]
            return True

    def move_left(pos):
        x, y = pos
        if x == 0 or map[y][x - 1] == ' ':
            for xx in range(WIDTH - 1, -1, -1):
                c = map[y][xx]
                if c == '#':
                    return False
                if c == '.':
                    pos[:] = [xx, y]
                    return True
        if map[y][x - 1] == '#':
            return False
        if map[y][x - 1] == '.':
            pos[:] = [x - 1, y]
            return True

    def move_down(pos):
        x, y = pos
        if y == HEIGHT - 1 or map[y + 1][x] == ' ':
            for yy in range(0, HEIGHT):
                c = map[yy][x]
                if c == '#':
                    return False
                if c == '.':
                    pos[:] = [x, yy]
                    return True
        if map[y + 1][x] == '#':
            return False
        if map[y + 1][x] == '.':
            pos[:] = [x, y + 1]
            return True

    def move_up(pos):
        x, y = pos
        if y == 0 or map[y - 1][x] == ' ':
            for yy in range(HEIGHT - 1, -1, -1):
                c = map[yy][x]
                if c == '#':
                    return False
                if c == '.':
                    pos[:] = [x, yy]
                    return True
        if map[y - 1][x] == '#':
            return False
        if map[y - 1][x] == '.':
            pos[:] = [x, y - 1]
            return True

    def move(pos: list, facing: str):
        if facing == '>':
            return move_right(pos)
        if facing == '<':
            return move_left(pos)
        if facing == 'v':
            return move_down(pos)
        return move_up(pos)

    moves_p1 = list(moves)
    while moves_p1:
        c = moves_p1.pop(0)
        if c == 'R':
            facing = turn_right[facing]
            continue
        if c == 'L':
            facing = turn_left[facing]
            continue

        while moves_p1 and moves_p1[0].isdigit():
            c += moves_p1.pop(0)
        c = int(c)

        for _ in range(c):
            if not move(pos, facing):
                break

    col, row = pos
    p1 = 1000 * (row + 1) + 4 * (col + 1) + facing_score[facing]
    print(f'{p1=}')

    facing = ['>']

    def move_cube(pos, facing):
        x, y = pos
        if facing[0] == '>':
            if x == (3 * SIZE - 1) and 0 <= y < (SIZE):
                yy = (3 * SIZE - 1) - y
                if map[yy][(2 * SIZE - 1)] in '.^>v<':
                    pos[:] = [(2 * SIZE - 1), yy]
                    facing[0] = '<'
                return map[yy][(2 * SIZE - 1)] in '.^>v<'
            if x == (2 * SIZE - 1) and (SIZE) <= y < (2 * SIZE):
                xx = y + (SIZE)
                if map[(SIZE - 1)][xx] in '.^>v<':
                    pos[:] = [xx, (SIZE - 1)]
                    facing[0] = '^'
                return map[(SIZE - 1)][xx] in '.^>v<'
            if x == (2 * SIZE - 1) and (2 * SIZE) <= y < (3 * SIZE):
                yy = (3 * SIZE - 1) - y
                if map[yy][(3 * SIZE - 1)] in '.^>v<':
                    pos[:] = [(3 * SIZE - 1), yy]
                    facing[0] = '<'
                return map[yy][(3 * SIZE - 1)] in '.^>v<'
            if x == (SIZE - 1) and (3 * SIZE) <= y < (4 * SIZE):
                xx = y - (2 * SIZE)
                if map[(3 * SIZE - 1)][xx] in '.^>v<':
                    pos[:] = [xx, (3 * SIZE - 1)]
                    facing[0] = '^'
                return map[(3 * SIZE - 1)][xx] in '.^>v<'
            if map[y][x + 1] in '.^>v<':
                pos[:] = [x + 1, y]
            return map[y][x + 1] in '.^>v<'
        if facing[0] == '<':
            if x == (SIZE) and 0 <= y < (SIZE):
                yy = (SIZE - 1) - y + (2 * SIZE)
                if map[yy][0] in '.^>v<':
                    pos[:] = [0, yy]
                    facing[0] = '>'
                return map[yy][0] in '.^>v<'
            if x == (SIZE) and (SIZE) <= y < (2 * SIZE):
                xx = y - (SIZE)
                if map[(2 * SIZE)][xx] in '.^>v<':
                    pos[:] = [xx, (2 * SIZE)]
                    facing[0] = 'v'
                return map[(2 * SIZE)][xx] in '.^>v<'
            if x == 0 and (2 * SIZE) <= y < (3 * SIZE):
                yy = (3 * SIZE - 1) - y
                if map[yy][(SIZE)] in '.^>v<':
                    pos[:] = [(SIZE), yy]
                    facing[0] = '>'
                return map[yy][(SIZE)] in '.^>v<'
            if x == 0 and (3 * SIZE) <= y < (4 * SIZE):
                xx = y - (2 * SIZE)
                if map[0][xx] in '.^>v<':
                    pos[:] = [xx, 0]
                    facing[0] = 'v'
                return map[0][xx] in '.^>v<'
            if map[y][x - 1] in '.^>v<':
                pos[:] = [x - 1, y]
            return map[y][x - 1] in '.^>v<'
        if facing[0] == 'v':
            if y == (SIZE - 1) and (2 * SIZE) <= x < (3 * SIZE):
                yy = x - (SIZE)
                if map[yy][(2 * SIZE - 1)] in '.^>v<':
                    pos[:] = [(2 * SIZE - 1), yy]
                    facing[0] = '<'
                return map[yy][(2 * SIZE - 1)] in '.^>v<'
            if y == (3 * SIZE - 1) and (SIZE) <= x < (2 * SIZE):
                yy = x + (2 * SIZE)
                if map[yy][(SIZE - 1)] in '.^>v<':
                    pos[:] = [(SIZE - 1), yy]
                    facing[0] = '<'
                return map[yy][(SIZE - 1)] in '.^>v<'
            if y == (4 * SIZE - 1) and 0 <= x < (SIZE):
                xx = x + (2 * SIZE)
                if map[0][xx] in '.^>v<':
                    pos[:] = [xx, 0]
                return map[0][xx] in '.^>v<'
            if map[y + 1][x] in '.^>v<':
                pos[:] = [x, y + 1]
            return map[y + 1][x] in '.^>v<'
        if facing[0] == '^':
            if y == (2 * SIZE) and 0 <= x < (SIZE):
                yy = x + (SIZE)
                if map[yy][(SIZE)] in '.^>v<':
                    pos[:] = [(SIZE), yy]
                    facing[0] = '>'
                return map[yy][(SIZE)] in '.^>v<'
            if y == 0 and (SIZE) <= x < (2 * SIZE):
                yy = x + (2 * SIZE)
                if map[yy][0] in '.^>v<':
                    pos[:] = [0, yy]
                    facing[0] = '>'
                return map[yy][0] in '.^>v<'
            if y == 0 and (2 * SIZE) <= x < (3 * SIZE):
                xx = x - (2 * SIZE)
                if map[(4 * SIZE - 1)][xx] in '.^>v<':
                    pos[:] = [xx, (4 * SIZE - 1)]
                return map[(4 * SIZE - 1)][xx] in '.^>v<'
            if map[y - 1][x] in '.^>v<':
                pos[:] = [x, y - 1]
            return map[y - 1][x] in '.^>v<'

    map = [list(r) for r in map]
    moves_p2 = list(moves)
    while moves_p2:
        c = moves_p2.pop(0)
        if c == 'R':
            facing[0] = turn_right[facing[0]]
            continue
        if c == 'L':
            facing[0] = turn_left[facing[0]]
            continue

        while moves_p2 and moves_p2[0].isdigit():
            c += moves_p2.pop(0)
        c = int(c)

        for _ in range(c):
            if not move_cube(pos2, facing):
                break

    col, row = pos2
    p2 = 1000 * (row + 1) + 4 * (col + 1) + facing_score[facing[0]]
    print(f'{p2=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '22.in'
    main(file)
