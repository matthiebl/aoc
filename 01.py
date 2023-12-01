#!/usr/bin/env python3.10

from sys import argv
import advent as adv

def main(file: str) -> None:
    print('Day 01')

    data = adv.input_as_lines(file)

if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '01.in'
    main(file)
