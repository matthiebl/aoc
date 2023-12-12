#!/usr/bin/env python3.10

from sys import argv
import advent as adv


def main(file: str) -> None:
    print('Day 09')

    data = adv.input_as_lines(file, map=adv.find_digits)

    p1 = 0
    p2 = 0
    for line in data:
        print(line)
        history: list[list[int]] = [line]
        while not all(n == 0 for n in history[-1]):
            new = []
            last = history[-1]
            for a, b in zip(last, last[1:]):
                new.append(b - a)
            history.append(new)
        history.reverse()
        history[0].append(0)
        for la, lb in zip(history, history[1:]):
            lb.append(lb[-1] + la[-1])
        p1 += history[-1][-1]

        history[0].insert(0, 0)
        for la, lb in zip(history, history[1:]):
            lb.insert(0, lb[0] - la[0])
            print(la, lb)
        print(history[-1][0])
        print()
        p2 += history[-1][0]

    print(f'{p1=}')
    print(f'{p2=}')

# p1=-115364


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '09.in'
    main(file)
