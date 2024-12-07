#!/usr/bin/env python3.12

import aocutils as u
from sys import argv

results = {"p1": set(), "p2": set()}


def try_calc(target: int, ns: list[int], curr: int, p2=False):
    key = "p2" if p2 else "p1"
    if target in results[key]:
        return
    if not ns and curr == target:
        results[key].add(target)
        return
    elif not ns:
        return

    cp = ns.copy()
    n = cp.pop(0)

    if curr == -1:
        try_calc(target, cp, n, p2)
    else:
        try_calc(target, cp, curr + n, p2)
        try_calc(target, cp, curr * n, p2)
        if p2:
            try_calc(target, cp, int(str(curr) + str(n)), p2)


def main(file: str) -> None:
    print('Day 07')

    data = [u.find_digits(line) for line in u.input_as_lines(file)]

    for [res, *ns] in data:
        try_calc(res, ns, -1)
    p1 = sum(results["p1"])
    print(f'{p1=}')

    for [res, *ns] in data:
        try_calc(res, ns, -1, p2=True)
    p2 = sum(results["p2"])
    print(f'{p2=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '07.in'
    main(file)
