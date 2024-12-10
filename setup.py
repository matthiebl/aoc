#!/usr/bin/env python3

from argparse import ArgumentParser
from os import chmod, path

from aocd import get_data

"""
Creation of script and input
"""

AOC_YEARS = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
AOC_URL = "https://adventofcode.com"


def create_input(day: int, year: int) -> None:
    data = get_data(day=day, year=year, block=True)
    with open(f"{day:02d}.in", "w") as f:
        f.write(data)
    print(f"\nPuzzle: {AOC_URL}/{year}/day/{day}")
    print(f"Input:  {AOC_URL}/{year}/day/{day}/input\n")


def create_script(day: int, year: int) -> None:
    if path.exists(f"{day:02d}.py") and input(f"{day:02d}.py already exists. Are you sure you want to overwrite? ") != "y":
        return
    with open(f"{day:02d}.py", "w") as f:
        f.write(
            f"""#!/usr/bin/env python3.13

from collections import Counter, defaultdict
from sys import argv
from maoc import fetch, submit
# from maoc.utils.classes import Point
# from maoc.utils.collect import chunks, windows
# from maoc.utils.parse import ints

\"\"\"
--- Day {day}: ---

{AOC_URL}/{year}/day/{day}
\"\"\"

print("Day {day:02d}")
FILE_NAME = argv[1] if len(argv) >= 2 else "{day:02d}.in"
raw = fetch(year={year}, day={day}, path=__file__, file_name=FILE_NAME)

def parse_raw():
    return raw.splitlines() # lines
    return [list(line) for line in raw.splitlines()] # grid
    return [group.splitlines() for group in raw.split("\\n\\n")] # grouped lines

data = parse_raw()
print(data)

def part_one():
    ...

def part_two():
    ...

p1 = part_one()
print(p1)
exit(0)  # Move as we go
submit(year={year}, day={day}, part=1, solution=p1, verbose=True)
p2 = part_two()
print(p2)
submit(year={year}, day={day}, part=2, solution=p2, verbose=True)
""")
    chmod(f"{day:02d}.py", 0o744)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("day", help="day of advent of code", type=int)
    parser.add_argument(
        "-y", "--year", help=f"year of advent of code, def: {AOC_YEARS[-1]}", type=int, default=AOC_YEARS[-1])
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "-s", "--script", help="create script file only", action="store_true")
    group.add_argument(
        "-i", "--input", help="get input file only", action="store_true")
    args = parser.parse_args()

    if args.year not in AOC_YEARS:
        print(f"AoC does not exist for year {args.year}!")
        exit()
    if args.script:
        create_script(args.day, args.year)
    elif args.input:
        create_input(args.day, args.year)
    else:
        create_script(args.day, args.year)
        # create_input(args.day, args.year)
