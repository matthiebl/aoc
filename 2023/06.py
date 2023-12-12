#!/usr/bin/env python3.10

from sys import argv
import aocutils as u


def ways(time, dist):
    beat = 0
    for t in range((time + 1) // 2):
        speed = t
        travel = speed * (time - t)
        if travel > dist:
            beat += 1
    return beat * 2 + (1 if time % 2 == 0 else 0)


def main(file: str) -> None:
    print('Day 06')

    data = u.input_as_lines(file)

    races = list(zip(u.find_digits(data[0]), u.find_digits(data[1])))

    p1 = 1
    for time, dist in races:
        p1 *= ways(time, dist)
    print(f'{p1=}')

    real_time = int(''.join(u.find_digits(data[0], map=str)))
    real_dist = int(''.join(u.find_digits(data[1], map=str)))
    p2 = ways(real_time, real_dist)
    print(f'{p2=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '06.in'
    main(file)
