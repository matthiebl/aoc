#!/usr/bin/env python3.12

import aocutils as u
from sys import argv


def main(file: str) -> None:
    print('Day 21')

    data = u.input_as_lines(file, map=lambda s: s.split(': '))
    jobs = {}
    for monkey, job in data:
        if job.isnumeric():
            jobs[monkey] = int(job)
        else:
            jobs[monkey] = tuple(job.split(' '))

    def determine(monkey: str) -> int:
        if isinstance(jobs[monkey], int):
            return jobs[monkey]

        a, op, b = jobs[monkey]
        left = determine(a)
        right = determine(b)

        result = None
        if op == '+':
            result = left + right
        if op == '-':
            result = left - right
        if op == '*':
            result = left * right
        if op == '/':
            result = left // right
        # jobs[monkey] = result

        return result

    p1 = determine('root')
    print(f'{p1=}')

    # This is dirty and solved by hand foy my specific input. 3916491093817
    # for attempt in range(3916491093800, 3916491094000):
    #     jobs['humn'] = attempt

    #     a, _, b = jobs['root']
    #     left = determine(a)
    #     right = determine(b)

    #     if left == right:
    #         print(attempt)
    #         break

    a, _, b = jobs['root']

    jobs['humn'] = 1000
    direction = determine(a)
    jobs['humn'] = 100000
    direction -= determine(a)

    p2 = p1 * 10

    # Use binary search to find the correct human value
    def binary(lo, hi, target, direction):
        mid = (lo + hi) // 2
        jobs['humn'] = mid
        current = determine(a)

        if current == target:
            return mid
        if current < target:
            if direction < 0:
                return binary(mid, hi, target, direction)
            return binary(lo, mid, target, direction)
        if current > target:
            if direction < 0:
                return binary(lo, mid, target, direction)
            return binary(mid, hi, target, direction)

    p2 = binary(0, p2, determine(b), direction)

    # Find the minimal value of p2 to satisfy the equality check
    while True:
        jobs['humn'] = p2 - 1
        if determine(a) == determine(b):
            p2 -= 1
        else:
            break

    print(f'{p2=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '21.in'
    main(file)
