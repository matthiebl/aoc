#!/usr/bin/env python3.12

import json
import os
import re
from argparse import ArgumentParser
from pathlib import Path
from time import time


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


def run_tests(args, answers: dict[str, dict[str, str]], tests: set[str]):
    tests = sorted(list(tests))

    total = 0
    for test in tests:
        start = time()
        s = os.popen(f'{args.solutions}/{test}.py {args.solutions}/{test}.in').read()
        end = time()
        total += end - start

        p1, p2 = answers[test]["p1"], answers[test]["p2"]
        a, b = True, True
        if p1 != "SKIP":
            a = re.search(f'p1[= ]*{p1}\n', s)
        if p2 != "SKIP":
            b = re.search(f'p2[= ]*{p2}\n', s)

        if not a or not b:
            print(f'Day {test} {colour.BOLD}{colour.FAIL}failed{colour.RESET}')
            print('===== OUTPUT =====')
            print(s)
        else:
            print(f'Day {test} {colour.BOLD}{colour.OKGREEN}passed{
                  colour.RESET} - in {end - start:.3f}s - {p1=}, {p2=}')

    print(f'Tests finished in {total:.3f}s')


if __name__ == '__main__':
    home = Path.home()
    with open(home / '.config/aocd/answers.json') as fp:
        answers: dict = json.load(fp)['answers']

    years = list(answers.keys())

    parser = ArgumentParser()
    parser.add_argument('solutions', type=str, metavar='PATH',
                        help='The path to the folder where a years of solutions are')
    parser.add_argument('-y', '--year', type=str, default=years[-1],
                        help=f'year of advent of code, default: {years[-1]}')
    parser.add_argument('--find-missing', type=str, metavar='DIRECTORY',
                        help='Searches the provided directory for solution scripts and finds which answers are missing from answers.json')
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        '-t', help='only run the provided tests', nargs='+', type=int)
    group.add_argument(
        '-x', help='exclude the provided tests', nargs='+', type=int)
    args = parser.parse_args()

    if args.year not in years:
        print(f'The provided year `{args.year}` is not within available list {years}')
        exit(1)

    available_tests = set(answers[args.year].keys())

    if args.find_missing:
        print("Not implemented yet")
        # print(args.find_missing)
        exit(0)

    if args.t:
        run_tests(args, answers[args.year], available_tests.intersection(
            set(map(lambda s: str(s).rjust(2, '0'), args.t))))
    elif args.x:
        run_tests(args, answers[args.year], available_tests - set(map(lambda s: str(s).rjust(2, '0'), args.x)))
    else:
        run_tests(args, answers[args.year], available_tests)
