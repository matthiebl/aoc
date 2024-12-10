from .constants import Constants


def parse_args(year: int, day: int) -> dict:
    """Simple argument parser implementation for script like execution"""
    from argparse import ArgumentParser

    parser = ArgumentParser(prog=f"aoc.{year}.{day:02d}", description=f"Advent of Code {year} Day {day}")
    input_args = parser.add_mutually_exclusive_group()
    input_args.add_argument("--example", "-ex", action="store_true", default=False)
    input_args.add_argument("--input", "-i", metavar="FILE", required=False,
                            default=Constants.input_file.format(year=year, day=f"{day:02d}"))
    args = parser.parse_args()

    print(f"Day {day} - Advent of Code {year}")

    return {
        "filename": Constants.example_file.format(year=year, day=f"{day:02d}") if args.example else args.input
    }


def get_input(filename: str, year: str, day: str) -> str:
    """
    Gets the input from a file. If the file does not exist, and
    fits for format of an input file, then the input is collected from aocd
    """
    from pathlib import Path
    from re import match

    if Path(filename).is_file():
        return open(filename).read()
    if match(Constants.input_file_re, filename):
        from aocd import get_data
        data = get_data(year=year, day=day, block=True)
        with open(filename, "w") as fp:
            fp.write(data)
        return data
    raise FileNotFoundError(f"Invalid filename provided: {filename}")
