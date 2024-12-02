#!/usr/bin/env python3.12

from sys import argv

import aocutils as u


def report_is_safe(report: list[int]) -> bool:
    diffs = [report[i] - report[i+1] for i in range(len(report) - 1)]
    return all(1 <= abs(x) <= 3 for x in diffs) and (all(x < 0 for x in diffs) or all(x > 0 for x in diffs))


def main(file: str) -> None:
    print('Day 02')

    data = u.input_as_lines(file, map=lambda x: u.map_int(x.split(' ')))

    p1 = 0
    p2 = 0
    for report in data:
        if report_is_safe(report):
            p1 += 1
        # Remove number one by one and check
        for i in range(len(report)):
            if report_is_safe(report[:i] + report[i+1:]):
                p2 += 1
                break
    print(f'{p1=}')
    print(f'{p2=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '02.in'
    main(file)
