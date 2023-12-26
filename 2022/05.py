#!/usr/bin/env python3.12

import aocutils as u
from sys import argv


def part1(stacks: list[list], moves: list[tuple]) -> str:
    for move in moves:
        amount, source, dest = move
        for _ in range(amount):
            box = stacks[source-1].pop(0)
            stacks[dest-1].insert(0, box)
    return ''.join(stack[0] for stack in stacks)


def part2(stacks: list[list], moves: list[tuple]) -> int:
    for move in moves:
        amount, source, dest = move
        boxes = stacks[source-1][:amount]
        stacks[source-1] = stacks[source-1][amount:]

        boxes.extend(stacks[dest-1])
        stacks[dest-1] = boxes
    return ''.join(stack[0] for stack in stacks)


def main(file: str) -> None:
    print('Day 05')

    [stack_data, moves] = u.input_from_grouped_lines(file)

    stacks = [list() for _ in range(1, len(stack_data[0]), 4)]
    for line in stack_data[:-1]:
        for i in range(1, len(line), 4):
            if line[i] != ' ':
                stacks[i//4].append(line[i])
    moves = [u.find_digits(line, group=tuple) for line in moves]

    p1 = part1([list(stack) for stack in stacks], moves)
    print(f'{p1=}')

    p2 = part2(stacks, moves)
    print(f'{p2=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '05.in'
    main(file)
