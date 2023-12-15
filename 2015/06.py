#!/usr/bin/env python3.12

import aocutils as u
from sys import argv


class AreaP1:
    def __init__(self, range, op, prev) -> None:
        self.x1 = range[0]
        self.y1 = range[1]
        self.x2 = range[2]
        self.y2 = range[3]

        self.op = op
        self.prev: AreaP1 = prev

    def status(self, x, y) -> bool:
        if self.x1 <= x <= self.x2 and self.y1 <= y <= self.y2:
            if self.op == 'off':
                return False
            elif self.op == 'on':
                return True
            else:
                return not self.prev.status(x, y)
        return self.prev.status(x, y)


class AreaP2:
    def __init__(self, range, instruction, prev) -> None:
        self.x1 = range[0]
        self.y1 = range[1]
        self.x2 = range[2]
        self.y2 = range[3]

        self.change = 2
        if instruction == 'on':
            self.change = 1
        elif instruction == 'off':
            self.change = -1
        self.prev: AreaP2 = prev

    def brightness(self, x, y) -> int:
        prev = self.prev.brightness(x, y) if self.prev is not None else 0
        if self.x1 <= x <= self.x2 and self.y1 <= y <= self.y2:
            return max(self.change + prev, 0)
        return prev


def main(file: str) -> None:
    print('Day 6')

    data = u.input_as_lines(file)

    instructions = AreaP1([0, 0, 999, 999], 'off', None)
    brightness = None

    for line in data:
        b = line.split()[1]
        op = 'toggle'
        if b == 'on' or b == 'off':
            op = b
        instructions = AreaP1(u.find_digits(line), op, instructions)
        brightness = AreaP2(u.find_digits(line), op, brightness)

    p1 = 0
    p2 = 0
    for x in range(0, 1000):
        for y in range(0, 1000):
            if instructions.status(x, y):
                p1 += 1
            p2 += brightness.brightness(x, y)

    print(f'{p1=}')
    print(f'{p2=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '06.in'
    main(file)
