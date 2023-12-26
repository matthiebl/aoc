#!/usr/bin/env python3.12

import aocutils as u
from sys import argv


def main(file: str) -> None:
    print('Day 11')

    raw_monkeys = [monkey[1:] for monkey in u.input_from_grouped_lines(file)]

    common = 1

    monkey_rules: list[tuple] = []
    monkey_items: list[list] = []
    for raw_monkey in raw_monkeys:
        items = list(map(int, raw_monkey[0][17:].split(', ')))
        operation = (raw_monkey[1][23:24], raw_monkey[1][25:])
        test = int(raw_monkey[2][21:])
        true = int(raw_monkey[3][29:])
        false = int(raw_monkey[4][30:])

        monkey_items.append(items)
        monkey_rules.append((operation, test, true, false))

        common *= test

    Monkeys = len(monkey_items)

    turns = [0] * Monkeys

    def round(p1=True):
        for monkey in range(Monkeys):
            while len(monkey_items[monkey]) > 0:
                (op, value), If, Then, Else = monkey_rules[monkey]
                item = monkey_items[monkey].pop(0)

                value = item if value == 'old' else int(value)

                if op == '*':
                    item *= value
                elif op == '+':
                    item += value

                if p1:
                    item = item // 3
                item = item % common

                monkey_items[Then if item % If == 0 else Else].append(item)
                turns[monkey] += 1

    for _ in range(20):
        round()
    turns.sort()

    p1 = turns[-1] * turns[-2]
    print(f'{p1=}')

    monkey_items: list[list] = []
    for raw_monkey in raw_monkeys:
        monkey_items.append(list(map(int, raw_monkey[0][17:].split(', '))))
    turns = [0] * Monkeys

    for r in range(10000):
        round(False)

    turns.sort()

    p2 = turns[-1] * turns[-2]
    print(f'{p2=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '11.in'
    main(file)
