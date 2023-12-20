#!/usr/bin/env python3.12

import aocutils as u
from sys import argv

INDEX = {'x': 0, 'm': 1, 'a': 2, 's': 3}


def is_accepted(RULES, r, nums):
    if r == 'A':
        return True
    if r == 'R':
        return False
    rules = RULES[r]
    for rule in rules:
        if ':' not in rule:
            if rule == 'A':
                return True
            if rule == 'R':
                return False
            return is_accepted(RULES, rule, nums)
        check, goto = rule.split(':')
        index = INDEX[check[0]]
        num = int(check[2:])
        if check[1] == '>' and nums[index] > num:
            return is_accepted(RULES, goto, nums)
        if check[1] == '<' and nums[index] < num:
            return is_accepted(RULES, goto, nums)


PREV = []


def intersection(xmas):
    count = 0
    for prev in PREV:
        prev = [(max(lo1, lo2), min(hi1, hi2))
                for (lo1, hi1), (lo2, hi2) in zip(xmas, prev)]
        if any(b - a <= 0 for a, b in prev):
            continue
        count += u.mul(b - a for a, b in prev)
        # for a in u.range_overlap(xmas[0], prev[0]):
        #     for b in u.range_overlap(xmas[1], prev[1]):
        #         for c in u.range_overlap(xmas[2], prev[0]):
        #             for d in u.range_overlap(xmas[3], prev[0]):
        #                 pass
        print(prev)
        print(*[u.range_overlap(r1, r2)
              for r1, r2 in zip(xmas, prev)], sep='\n')
        print()
    PREV.append(xmas)
    return count


def send(RULES, r, xmas):
    if any(b - a <= 0 for a, b in xmas) or r == 'R':
        return 0
    if r == 'A':
        count = u.mul(b - a for a, b in xmas)
        copies = intersection(xmas)
        print(xmas, count, copies)
        return count - copies
    rules = RULES[r]
    xxmas = xmas.copy()

    total = 0
    for rule in rules:
        if ':' not in rule:
            return total + send(RULES, rule, xmas)
        check, goto = rule.split(':')
        index = INDEX[check[0]]
        num = int(check[2:])
        lo, hi = xxmas[index]
        xxxmas = xxmas.copy()
        if check[1] == '>':
            xxxmas[index] = (max(lo, num), hi)
            total += send(RULES, goto, xxxmas)
            xxmas[index] = (lo, min(hi, num))
        elif check[1] == '<':
            xxxmas[index] = (lo, min(hi, num))
            total += send(RULES, goto, xxxmas)
            xxmas[index] = (max(lo, num), hi)
    return total


def main(file: str) -> None:
    print('Day 19')

    [inst, coords] = u.input_from_grouped_lines(file)

    I = {}
    for ins in inst:
        name, rules = ins.split('{')
        rules = rules[:-1].split(',')
        I[name] = rules

    p1 = 0
    for coord in coords:
        nums = u.find_digits(coord)
        if is_accepted(I, 'in', nums):
            p1 += sum(nums)
    print(f'{p1=}')

    p2 = send(I, 'in', [(1, 4001), (1, 4001), (1, 4001), (1, 4001)])
    print(f'{p2=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '19.in'
    main(file)
