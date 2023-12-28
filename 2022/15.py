#!/usr/bin/env python3.12

import aocutils as u
from sys import argv

TUNING_FREQ = 4000000


def detected_intervals(sensors, y: int) -> list[tuple[int, int]]:
    intervals = []

    for sx, sy, bx, by in sensors:
        d = u.manhattan_dist(sx, sy, bx, by)
        off = d - abs(sy - y)
        if off < 0:
            continue
        lx = sx - off
        hx = sx + off
        intervals.append((lx, hx + 1))

    return u.merge_intervals(intervals)


def main(file: str) -> None:
    print('Day 15')

    Y_RANGE = 20 if file == '15.ex' else 4000000
    Y_CHECK = 10 if file == '15.ex' else 2000000

    sensors = u.input_as_lines(file, map=lambda s: u.find_digits(s))

    merged = detected_intervals(sensors, Y_CHECK)
    assert len(merged) == 1
    p1 = merged[0][1] - 1 - merged[0][0]
    print(f'{p1=}')

    p2 = 0
    for y in range(Y_RANGE + 1):
        merged = detected_intervals(sensors, y)
        if len(merged) == 2:
            p2 = merged[0][1] * TUNING_FREQ + y
            break
    print(f'{p2=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '15.in'
    main(file)
