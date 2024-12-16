from dataclasses import dataclass
from .constants import Constants


@dataclass
class Args:
    from typing import Callable

    filename: str
    test: bool
    tester: Callable[[int, int], bool]

    def __getitem__(self, item):
        return getattr(self, item)


def parse_args(year: int, day: int) -> Args:
    """Simple argument parser implementation for script like execution"""
    from argparse import ArgumentParser

    default_input = Constants.input_file.format(year=year, day=f"{day:02d}")
    default_example = Constants.example_file.format(year=year, day=f"{day:02d}")
    parser = ArgumentParser(prog=f"aoc.{year}.{day:02d}", description=f"Advent of Code {year} Day {day}")
    input_args = parser.add_mutually_exclusive_group()
    input_args.add_argument("--example", "-ex", action="store_true", default=False,
                            help=f"Whether to use example extension, eg: {default_example}")
    input_args.add_argument("--input", "-i", metavar="FILE", required=False, default=default_input,
                            help=f"Input file to read from, default: {default_input}")
    parser.add_argument("--test", "-t", action="store_true", default=False,
                        help="Whether to assert the answers are correct, ignored with --example flag, default: False")
    args = parser.parse_args()

    print(f"Day {day} - Advent of Code {year}")

    return Args(
        filename=default_example if args.example else args.input,
        test=args.test and not args.example,
        tester=answer_tester(year, day),
    )


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


def answer_tester(year: str, day: str):
    """Gets the answers from the answers"""
    from .answers import get_answers
    answers = get_answers(year, day)

    def inner(p1, p2):
        if answers is None:
            print("No stored answers for {year} day {day}")
            return False
        assert p1 == answers["p1"], f"Part 1: {p1} is not expected {answers["p1"]}"
        assert p2 == answers["p2"], f"Part 2: {p2} is not expected {answers["p2"]}"
        return True
    return inner
