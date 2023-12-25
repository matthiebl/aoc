#!/usr/bin/env python3.12

from argparse import ArgumentParser
import os
import re
from time import time


TESTS = {
    '01': (54940, 54208),             # 0.043s
    '02': (2101, 58269),              # 0.027s
    '03': (535078, 75312571),         # 0.029s
    '04': (15205, 6189740),           # 0.028s
    '05': (31599214, 20358599),       # 0.030s
    '06': (1195150, 42550411),        # 1.573s
    '07': (253313241, 253362743),     # 0.032s
    '08': (22199, 13334102464297),    # 0.040s
    '09': (1868368343, 1022),         # 0.028s
    '10': (7102, 363),                # 0.054s
    '11': (9214785, 613686987427),    # 0.056s
    '12': (7716, 18716325559999),     # 0.886s
    '13': (27300, 29276),             # 0.094s
    '14': (108935, 100876),           # 0.409s
    '15': (505459, 228508),           # 0.030s
    '16': (7199, 7438),               # 1.056s
    '17': (1039, 1201),               # 1.549s
    '18': (40131, 104454050898331),   # 1.549s
    '19': (319295, 110807725108076),  # 0.035s
    '20': (808146535, None),          #
    '21': (3605, None),               #
    '22': (473, None),                #
    '23': (2166, 6378),               # 13.060s
    '24': (17906, 571093786416929),   # 0.421s
    '25': (506202, None),             # 2.098s
}


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
