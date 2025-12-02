"""Command-line interface for AoC solver."""

import argparse
import sys
from importlib import import_module
from pathlib import Path

from rich.console import Console
from rich.panel import Panel

from advent.core.fetcher import fetch_input
from advent.core.utils import timing

console = Console()


def create_day_template(year: int, day: int) -> None:
    """Create a new day solution template."""
    year_dir = Path(f"src/advent/solutions/year_{year}")
    year_dir.mkdir(parents=True, exist_ok=True)

    # Create __init__.py if it doesn't exist
    init_file = year_dir / "__init__.py"
    if not init_file.exists():
        init_file.write_text(f'"""Solutions for Advent of Code {year}."""\n')

    day_file = year_dir / f"day_{day:02d}.py"
    if day_file.exists():
        console.print(f"[yellow]Day {day} already exists![/yellow]")
        return

    template = f'''"""
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

    day_file.write_text(template)
    console.print(f"[green]✓[/green] Created {day_file}")

    # Fetch input
    try:
        input_path = Path(f"inputs/{year}/day_{day:02d}.txt")
        fetch_input(year, day, input_path)
        console.print(f"[green]✓[/green] Downloaded input to {input_path}")
    except Exception as e:
        console.print(f"[yellow]⚠[/yellow] Could not fetch input: {e}")


def run_solution(year: int, day: int) -> None:
    """Run a solution for a specific day."""
    try:
        module = import_module(f"advent.solutions.year_{year}.day_{day:02d}")
        solver_class = getattr(module, f"Day{day:02d}")

        solver = solver_class(year, day)
        solver.load_input()

        console.print(
            Panel(f"[bold cyan]Advent of Code {year} - Day {day}[/bold cyan]", expand=False)
        )

        solver.prepare()

        @timing
        def solve_part1() -> int:
            return solver.part1()

        @timing
        def solve_part2() -> int:
            return solver.part2()

        result1 = solve_part1()
        console.print(f"[green]Part 1:[/green] {result1}")

        result2 = solve_part2()
        console.print(f"[green]Part 2:[/green] {result2}")

    except ModuleNotFoundError:
        console.print(
            f"[red]✗[/red] Solution for day {day} not found. Create it with: aoc new {year} {day}"
        )
        sys.exit(1)
    except FileNotFoundError as e:
        console.print(f"[red]✗[/red] {e}")
        sys.exit(1)


def main() -> None:
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(prog="aoc", description="Advent of Code solver toolkit")

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # New command
    new_parser = subparsers.add_parser("new", help="Create a new day solution")
    new_parser.add_argument("year", type=int, help="Year (e.g., 2024)")
    new_parser.add_argument("day", type=int, help="Day (1-25)")

    # Run command
    run_parser = subparsers.add_parser("run", help="Run a solution")
    run_parser.add_argument("year", type=int, help="Year (e.g., 2024)")
    run_parser.add_argument("day", type=int, help="Day (1-25)")

    args = parser.parse_args()

    if args.command == "new":
        create_day_template(args.year, args.day)
    elif args.command == "run":
        run_solution(args.year, args.day)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
