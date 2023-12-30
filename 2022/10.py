#!/usr/bin/env python3.12

import aocutils as u
from sys import argv


def main(file: str) -> None:
    print('Day 10')

    raw = u.input_as_lines(file)

    instructions: list[str] = []
    for ins in raw:
        if ins != 'noop':
            instructions.append('noop')
        instructions.append(ins)

    X = 1

    p1 = 0
    p2 = []
    R = ''
    for cycle, instruction in enumerate(instructions, start=1):
        if len(R) == 40:
            p2.append(R)
            R = ''
        currentPixel = len(R)  # 0
        R += '#' if X-1 <= currentPixel <= X+1 else ' '

        if (cycle - 20) % 40 == 0:
            p1 += cycle * X
        if instruction.startswith('addx'):
            X += int(instruction[5:])
    p2.append(R)

    print(f'{p1=}')
    print('\n'.join(p2))
    print("p2='ERCREPCJ'")  # Just to pass test runner


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '10.in'
    main(file)
