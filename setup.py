#!/usr/bin/env python3

from argparse import ArgumentParser
from aocd import get_data, exceptions
from os import chmod, path

"""
Creation of script and input
"""

AOC_YEARS = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]


def create_input(day: int, year: int) -> None:
    try:
        data = get_data(day=day, year=year)
    except exceptions.PuzzleLockedError:
        print(f'AoC {year} day {day} not available yet!')
        exit()
    with open(f'{day:02d}.in', 'w') as f:
        f.write(data)


def create_script(day: int) -> None:
    if path.exists(f'{day:02d}.py') and input(f'{day}.py already exists. Are you sure you want to overwrite? ') != 'y':
        return
    with open(f'{day:02d}.py', 'w') as f:
        f.write(
            f"""#!/usr/bin/env python3.12

import aocutils as u
from sys import argv

def main(file: str) -> None:
    print('Day {day}')

    data = u.input_as_lines(file)
    print(data)

if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '{day:02d}.in'
    main(file)
""")
    chmod(f'{day:02d}.py', 0o744)


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('day', help='day of advent of code', type=int)
    parser.add_argument(
        '-y', '--year', help=f'year of advent of code, def: {AOC_YEARS[-1]}', type=int, default=AOC_YEARS[-1])
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        '-s', '--script', help='create script file only', action='store_true')
    group.add_argument(
        '-i', '--input', help='get input file only', action='store_true')
    args = parser.parse_args()

    if args.year not in AOC_YEARS:
        print(f'AoC does not exist for year {args.year}!')
        exit()
    if args.script:
        create_script(args.day)
    elif args.input:
        create_input(args.day, args.year)
    else:
        create_input(args.day, args.year)
        create_script(args.day)
