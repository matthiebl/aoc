#!/usr/bin/env python3.12

from argparse import ArgumentParser
import os
import re
from time import time


TESTS = {
    '01': (71934, 211447),                   # 0.033s
    '02': (12772, 11618),                    # 0.026s
    '03': (8243, 2631),                      # 0.028s
    '04': (515, 883),                        # 0.028s
    '05': ("'JRVNHHCSJ'", "'GNFBSBJLH'"),    # 0.027s
    '06': (1361, 3263),                      # 0.028s
    '07': (919137, 2877389),                 # 0.026s
    '08': (1776, 234416),                    # 0.054s
    '09': (6284, 2661),                      # 0.067s
    '10': (11720, 'ERCREPCJ'),               # 0.031s
    '11': (72884, 15310845153),              # 0.165s
    '12': (370, 363),                        # 1.049s
    '13': (5717, 25935),                     # 0.041s
    '14': (1078, 30157),                     # 0.468s
    '15': (5403290, 10291582906626),         # 17.137s
    '16': (1474, 2100),                      # 12.356s
    '17': (3147, 1532163742758),             # 0.069s
    '18': (3586, 2072),                      # 0.042s
    '19': (1346, 7644),                      # 1.248s
    '20': (3473, 7496649006261),             # 3.507s
    '21': (72664227897438, 3916491093817),   # 0.042s
    '22': (189140, 115063),                  # 0.044s
    '23': (4146, 957),                       # 4.600s
    '24': (274, 839),                        # 1.377s
    '25': ("'2=-0=01----22-0-1-10'", None),  # 0.040s
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
