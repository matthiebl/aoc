#!/usr/bin/env python3.12

from sys import argv

import aocutils as u


def rules_pass(rules: list, update: list):
    for [ra, rb] in rules:
        try:
            ai = update.index(ra)
            bi = update.index(rb)
        except ValueError:
            continue

        if ai >= bi:
            return False
    return True


def main(file: str) -> None:
    print('Day 05')

    rules, updates = u.input_from_grouped_lines(file)
    rules = [u.map_int(rule.split('|')) for rule in rules]
    updates = [u.map_int(update.split(',')) for update in updates]

    bad_updates: list[list[int]] = []
    p1 = 0
    for update in updates:
        if rules_pass(rules, update):
            p1 += update[len(update) // 2]
        else:
            bad_updates.append(update)

    print(f'{p1=}')

    p2 = 0
    for update in bad_updates:
        ordered: list[int] = []
        while update:
            valid_rules = []
            for [ra, rb] in rules:
                try:
                    update.index(ra)
                    update.index(rb)
                except ValueError:
                    continue
                valid_rules.append([ra, rb])

            for n in update:
                bad = False
                for [ra, rb] in valid_rules:
                    if n == ra:
                        bad = True
                        break
                if not bad:
                    ordered.append(n)
                    update.remove(n)
                    break

        p2 += ordered[len(ordered) // 2]

    print(f'{p2=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '05.in'
    main(file)
