"""Command-line interface for AoC solver."""

import argparse
import re
import sys
from importlib import import_module
from pathlib import Path

from rich.console import Console
from rich.panel import Panel

from advent.core.fetcher import fetch_input
from advent.core.solver import Solver
from advent.core.utils import timing

console = Console()


def main() -> None:
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(prog="aoc", description="Advent of Code solver toolkit")

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # New command
    new_parser = subparsers.add_parser("new", help="Create a new day solution")
    new_parser.add_argument("year", type=int, help="Year (e.g., 2015)")
    new_parser.add_argument("day", type=int, help="Day (1-25)")

    # Run command
    run_parser = subparsers.add_parser("run", help="Run a solution")
    run_parser.add_argument("year", type=int, help="Year (e.g., 2015)")
    run_parser.add_argument("day", type=int, help="Day (1-25)")
    run_parser.add_argument("--input", "-i", type=str, help="Alternate input file path")
    run_parser.add_argument(
        "--parts",
        "-p",
        nargs="+",
        default=[1, 2],
        type=int,
        help="Alternate input file path",
    )

    # Test command
    test_parser = subparsers.add_parser("test", help="Test a year of solutions")
    test_parser.add_argument("year", type=int, help="Year (e.g., 2015)")

    args = parser.parse_args()

    if args.command == "new":
        create_day_template(args.year, args.day)
    elif args.command == "run":
        run_solution(args.year, args.day, args.input, args.parts)
    elif args.command == "test":
        test_solutions(args.year)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()


TEMPLATE = '''"""
--- Day {day}: ... ---
https://adventofcode.com/{year}/day/{day}
"""

from advent.core import Solver


class Day{day:02d}(Solver):
    """Solution for day {day}."""

    def prepare(self):
        pass

    def part1(self) -> int:
        """Solve part 1."""
        lines = self.input.lines()
        # TODO: Implement solution
        return 0

    def part2(self) -> int:
        """Solve part 2."""
        lines = self.input.lines()
        # TODO: Implement solution
        return 0
'''

INIT_TEMPLATE = '''"""Solutions for Advent of Code {year}."""

answers = {{}}
'''


def create_day_template(year: int, day: int) -> None:
    """Create a new day solution template."""

    year_dir = Path(f"src/advent/solutions/year_{year}")
    year_dir.mkdir(parents=True, exist_ok=True)

    # Create __init__.py if it doesn't exist
    init_file = year_dir / "__init__.py"
    if not init_file.exists():
        init_file.write_text(INIT_TEMPLATE.format(year=year))

    day_file = year_dir / f"day_{day:02d}.py"
    if day_file.exists():
        console.print(f"[yellow]Day {day} already exists![/yellow]")
        return

    template = TEMPLATE.format(year=year, day=day)

    day_file.write_text(template)
    console.print(f"[green]✓[/green] Created {day_file}")

    # Fetch input
    try:
        input_path = Path(f"inputs/{year}/day_{day:02d}.txt")
        fetch_input(year, day, input_path)
        console.print(f"[green]✓[/green] Downloaded input to {input_path}")
    except Exception as e:
        console.print(f"[yellow]⚠[/yellow] Could not fetch input: {e}")


def run_solution(year: int, day: int, input_path: str | None, parts: list[int]) -> None:
    """Run a solution for a specific day."""
    try:
        if input_path is None:
            _get_default_solution_input(year, day)

        solver = _get_solver(year, day)
        solver.load_input(input_path)

        console.print(
            Panel(f"[bold cyan]Advent of Code {year} - Day {day}[/bold cyan]", expand=False)
        )

        @timing
        def solve_part1() -> int:
            return solver.part1()

        @timing
        def solve_part2() -> int:
            return solver.part2()

        answers = _get_answers(year)
        answer1, answer2 = answers.get(day, (None, None))

        solver.prepare()
        if 1 in parts:
            result1 = solve_part1()
            colour = _get_answer_colour(result1, answer1)
            console.print(f"Part 1: [{colour}]{result1}[/]")
        if 2 in parts:
            result2 = solve_part2()
            colour = _get_answer_colour(result2, answer2)
            console.print(f"Part 2: [{colour}]{result2}[/]")

    except FileNotFoundError as e:
        console.print(f"[red]✗[/red] {e}")
        sys.exit(1)


def test_solutions(year: int) -> None:
    existing_solutions = []
    for file in Path(f"src/advent/solutions/year_{year}").glob("**/*day_*.py"):
        match = re.search(r"day_(\d\d).py", file.as_posix())
        existing_solutions.append(int(match.group(1)))
    existing_solutions.sort()

    console.print(
        Panel(f"[bold cyan]Advent of Code {year} - Benchmark Test[/bold cyan]", expand=False)
    )

    total_time = 0
    correct = 0

    for day in existing_solutions:
        solver = _get_solver(year, day)
        solver.load_input()
        solver.prepare()
        console.print(f"[bold cyan]Day {day}[/bold cyan]")

        @timing(store=True, verbose=False)
        def solve_part1() -> int:
            return solver.part1()

        @timing(store=True, verbose=False)
        def solve_part2() -> int:
            return solver.part2()

        answers = _get_answers(year)
        answer1, answer2 = answers.get(day, (None, None))

        solver.prepare()
        result1, time1 = solve_part1()
        colour = _get_answer_colour(result1, answer1)
        console.print(f"Part 1: [{colour}]{result1}[/] ({time1}ms)")
        total_time += time1
        correct += 1 if colour == "green" else 0

        result2, time2 = solve_part2()
        colour = _get_answer_colour(result2, answer2)
        console.print(f"Part 2: [{colour}]{result2}[/] ({time2}ms)")
        total_time += time2
        correct += 1 if colour == "green" else 0

        console.print("")

    total_answers = len(existing_solutions) * 2
    incorrect = total_answers - correct

    correct_msg = f"[green]{correct} correct[/]" if correct else ""
    incorrect_msg = f"[red]{incorrect} incorrect[/]" if incorrect else ""
    result_msg = " ".join(filter(lambda x: bool(x), [correct_msg, incorrect_msg]))
    console.print(f"Result: {result_msg} out of {total_answers}")
    console.print(f"Total time: [bold cyan]{total_time:.2f}[/]ms")


def _get_solver(year: int, day: int) -> Solver:
    try:
        module = import_module(f"advent.solutions.year_{year}.day_{day:02d}")
        solver_class = getattr(module, f"Day{day:02d}")

        return solver_class(year, day)
    except ModuleNotFoundError:
        console.print(
            f"[red]✗[/red] Solution for day {day} not found. Create it with: aoc new {year} {day}"
        )
        sys.exit(1)


def _get_default_solution_input(year: int, day: int) -> None:
    default_input = Path(f"inputs/{year}/day_{day:02d}.txt")
    if not default_input.exists():
        console.print(f"[yellow]Input file not found: {default_input}[/yellow]")
        response = console.input("[bold]Fetch input from Advent of Code? (y/N): [/bold]")
        if response.lower() in ("y", "yes"):
            try:
                fetch_input(year, day, default_input)
                console.print(f"[green]✓[/green] Downloaded input to {default_input}")
            except Exception as e:
                console.print(f"[red]✗[/red] Failed to fetch input: {e}")
                sys.exit(1)
        else:
            console.print("[red]✗[/red] Cannot run without input file")
            sys.exit(1)


def _get_answers(year: int) -> dict[str, tuple]:
    try:
        module = import_module(f"advent.solutions.year_{year}")
        answers = getattr(module, "answers")
        return answers
    except ModuleNotFoundError:
        console.print(f"[red]✗[/red] Cannot find base init module for year {year}.")
    except AttributeError:
        pass
    return {}


def _get_answer_colour(actual, expected) -> str:
    if actual == expected:
        return "green"
    elif expected is None:
        return "default"
    return "red"
