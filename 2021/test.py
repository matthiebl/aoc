#!/usr/bin/env python3.12

from argparse import ArgumentParser
import os
import re
from time import time


TESTS = {
    '01': (1766, 1797),             # 0.031s
    '02': (1815044, 1739283308),    # 0.026s
    '03': (2498354, 3277956),       # 0.029s
    '04': (38594, 21184),           # 0.177s
    '05': (4993, 21101),            # 0.113s
    '06': (386536, 1732821262171),  # 0.028s
    '07': (356958, 105461913),      # 0.219s
    '08': (548, 1074888),           #
    '09': (558, 882942),            # 0.038s
    '10': (290691, 2768166558),     # 0.026s
    '11': (1757, 422),              # 0.040s
    '12': (4707, 130493),           # 0.212s
    '13': (788, "'KJBKEUBG'"),      # 0.027s
    '14': (3259, 3459174981021),    # 0.026s
    '15': (604, 2907),              # 0.409s
    '16': (974, 180616437720),      # 0.033s
    '17': (5460, 3618),             # 0.120s
    '18': (3665, 4775),             # 1.077s
    '19': (None, None),             #
    '20': (None, None),             #
    '21': (None, None),             #
    '22': (None, None),             #
    '23': (None, None),             #
    '24': (None, None),             #
    '25': (None, None),             #
}
# Tests finished in 42.519s


class colour:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def run_tests(tests: set[str]):
    tests = sorted(list(tests))

    total = 0
    for test in tests:
        if test not in TESTS:
            print(f'Test {test} {colour.BOLD}{colour.WARNING}skipped{
                  colour.RESET} - no such test')
            continue

        start = time()
        s = os.popen(f'./{test}.py').read()
        end = time()
        total += end - start

        p1, p2 = TESTS[test]
        a, b = True, True
        if p1:
            a = re.search(f'p1={p1}\n', s)
        if p2:
            b = re.search(f'p2={p2}\n', s)

        if not a or not b:
            print(f'Day {test} {colour.BOLD}{
                  colour.FAIL}failed{colour.RESET}')
            print('===== OUTPUT =====')
            print(s)
        else:
            print(f'Day {test} {colour.BOLD}{colour.OKGREEN}passed{
                colour.RESET} - in {end - start:.3f}s - {p1=}, {p2=}')

    print(f'Tests finished in {total:.3f}s')


if __name__ == '__main__':
    parser = ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        '-t', help='only run the provided tests', nargs='+', type=int)
    group.add_argument(
        '-x', help='exclude the provided tests', nargs='+', type=int)
    args = parser.parse_args()

    all_tests = set(TESTS.keys())
    if args.t:
        run_tests(set(map(lambda s: str(s).rjust(2, '0'), args.t)))
    elif args.x:
        run_tests(all_tests - set(map(lambda s: str(s).rjust(2, '0'), args.x)))
    else:
        run_tests(all_tests)
