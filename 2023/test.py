#!/usr/bin/env python3.12

import os
import re
from io import StringIO


TESTS = {
    '01': (54940, 54208),
    '02': (2101, 58269),
    '03': (535078, 75312571),
    '04': (15205, 6189740),
    '05': (31599214, 20358599),
    '06': (1195150, 42550411),
    '07': (253313241, 253362743),
    '08': (22199, 13334102464297),
    '09': (1868368343, 1022),
    '10': (7102, 363),
    '11': (9214785, 613686987427),
    '12': (7716, 18716325559999),
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


for test in TESTS:
    s = os.popen(f'./{test}.py').read()
    p1, p2 = TESTS[test]
    a = re.search(f'p1={p1}\n', s)
    b = re.search(f'p2={p2}\n', s)
    if not a or not b:
        print(f'Test {test} {colour.BOLD}{colour.FAIL}failed{colour.RESET}')
        print('===== OUTPUT =====')
        print(s)
    else:
        print(f'Test {test} {colour.BOLD}{colour.OKGREEN}passed{
              colour.RESET} - {p1=}, {p2=}')
