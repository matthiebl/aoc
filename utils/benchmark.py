from contextlib import redirect_stdout
from enum import Enum
from importlib import import_module
from io import StringIO
from pathlib import Path
import sys
from time import time
from .answers import get_answers


class Colour:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'


class SolutionStatus(Enum):
    WAIT = 0
    PASS = 1
    COMP = 2
    FAIL = 3
    SKIP = 4


def benchmark(year: str, timeout: int = 600):
    data = {"time": 0, "tests": {}}

    for day in range(1, 25 + 1):
        day_s = f"{day:02d}"
        print(f"Day {day_s}", end=" ", flush=True)
        info = {"status": SolutionStatus.WAIT, "time": 0, "stdout": "(None)", "stderr": "(None)", "logs": "(None)"}

        if data["time"] / 1000 > timeout:
            print(f"{Colour.WARNING}SKIPPED{Colour.RESET} (timeout)")
            info["status"] = SolutionStatus.SKIP
            continue

        print("...", end="", flush=True)

        f = StringIO()
        with redirect_stdout(f):
            if Path(f"{year}/{day_s}.py").is_file():
                fm = StringIO()
                with redirect_stdout(fm):
                    t0 = time()

                    try:
                        module = import_module(f"{year}.{day_s}")
                    except Exception as e:
                        info["status"] = SolutionStatus.FAIL
                        info["stderr"] = str(e)
                        print(e)
                    p1 = getattr(module, "p1")
                    p2 = getattr(module, "p2")

                    t1 = time()

                ms = (t1 - t0) * 1000
                data["time"] += ms
                info["time"] = ms
                info["stdout"] = fm.getvalue()

                if info["status"] == SolutionStatus.FAIL:
                    print("Unhandled exception caught:")
                    print("--- STDERR ---")
                    print(str(e))

                print(f"Solution ran in: {ms:.3f}ms")

                answers = get_answers(year, day_s)
                if answers is None:
                    print(f"No answers for {year} day {day}")
                    info["status"] = SolutionStatus.COMP
                elif p1 == answers["p1"] and p2 == answers["p2"]:
                    info["status"] = SolutionStatus.PASS
                elif p1 is not None and p2 is not None:
                    print(f"Answers in solution for {year} day {day} do no match expected")
                    print("--- STDOUT ---")
                    print(info["stdout"])
                    print("--- EXPECTED ---")
                    print(f"p1={answers["p1"]}")
                    print(f"p2={answers["p2"]}")
                    info["status"] = SolutionStatus.FAIL

            else:
                print(f"Solution for {year} day {day} ({year}/{day_s}.py) is missing")
                info["status"] = SolutionStatus.SKIP

        sys.stdout.write("\b\b\b")
        sys.stdout.flush()
        match info["status"]:
            case SolutionStatus.PASS:
                print(f"{Colour.GREEN}PASSED{Colour.RESET} [{info["time"]:.03f}ms]")
            case SolutionStatus.COMP:
                print(f"{Colour.CYAN}PASSED{Colour.RESET} [{info["time"]:.03f}ms] (no answers)")
            case SolutionStatus.FAIL:
                print(f"{Colour.FAIL}FAILED{Colour.RESET}")
            case SolutionStatus.SKIP:
                print(f"{Colour.WARNING}SKIPPED{Colour.RESET} (no solution)")

        if data["time"] / 1000 > timeout:
            print("Timeout exceeded. Skipping remaining tests...")
        info["logs"] = f.getvalue()
        data["tests"][day] = info

    return data


def header(year: str):
    ...


def summary(data: dict):
    ...


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser(description=f"Advent of Code Benchmarker")
    parser.add_argument("year", help="The year to test and benchmark")
    parser.add_argument("--timeout", type=int, default=600,
                        help="The seconds to quit benchmarking if exceeded after each day. default: 600")
    args = parser.parse_args()

    benchmark(args.year, timeout=args.timeout)
