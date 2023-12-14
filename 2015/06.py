#!/usr/bin/env python3.12

import aocutils as u
from sys import argv

def main(file: str) -> None:
    print('Day 6')

    data = u.input_as_lines(file)
    print(data)

if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '06.in'
    main(file)
