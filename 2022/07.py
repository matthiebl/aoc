#!/usr/bin/env python3.12

import aocutils as u
from sys import argv


def main(file: str) -> None:
    print('Day 07')

    terminal = [query.split('\n')[:-1]
                for query in (u.read_input(file) + '\n').split('$ ')][1:]
    cwd = []
    system = {}
    for result in terminal:
        cmd = result.pop(0)
        if cmd.startswith('cd'):
            path = cmd.split(' ')[1]
            if path == '/':
                cwd = ['~']
            elif path == '..':
                cwd.pop()
            else:
                cwd.append(path)
            continue

        pwd = '/'.join(cwd)
        cd = []
        for file in result:
            a, b = file.split(' ')
            if a == 'dir':
                this = ('d', f'{pwd}/{b}')
                cd.append(this)
            else:
                cd.append(('f', int(a)))
        system[pwd] = cd

    sizes = {}

    def size(d):
        if d in sizes:
            return sizes[d]

        total = 0
        for typ, data in system[d]:
            if typ == 'f':
                total += data
            else:
                total += size(data)
        sizes[d] = total
        return total

    size('~')

    free = 70_000_000 - sizes['~']
    needed = 30_000_000 - free

    p1 = 0
    possible = []
    for dsize in sizes.values():
        if dsize <= 100000:
            p1 += dsize
        if dsize >= needed:
            possible.append(dsize)
    print(f'{p1=}')
    p2 = min(possible)
    print(f'{p2=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '07.in'
    main(file)
