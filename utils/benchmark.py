from contextlib import redirect_stdout
from enum import Enum
from importlib import import_module
from io import StringIO
from pathlib import Path
import signal
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
    TIMEOUT = 5


def timeout_handler(signum, frame):
    raise TimeoutError("Timed out!")


def benchmark(args):
    header(args)

    year = args.year
    timeout = args.timeout
    executions = args.attempts

    data = {"time": 0, "tests": {}}

    for day in range(1, 25 + 1):
        day_s = f"{day:02d}"
        print(f"Day {day_s}", end=" ", flush=True)
        info = {"status": SolutionStatus.WAIT, "time": 0, "stdout": "(None)", "stderr": "(None)", "logs": "(None)"}

        print("...", end="", flush=True)

        f = StringIO()
        with redirect_stdout(f):
            if Path(f"{year}/{day_s}.py").is_file():
                fm = StringIO()
                with redirect_stdout(fm):
                    t0 = time()

                    p1, p2 = None, None
                    try:
                        signal.signal(signal.SIGALRM, timeout_handler)
                        signal.alarm(timeout)
                        module = import_module(f"{year}.{day_s}")
                        p1 = getattr(module, "p1")
                        p2 = getattr(module, "p2")
                    except TimeoutError:
                        info["status"] = SolutionStatus.TIMEOUT
                        info["stderr"] = f"Exceeded {timeout} seconds"
                    except Exception as e:
                        info["status"] = SolutionStatus.FAIL
                        info["stderr"] = str(e)
                        print(e)
                    finally:
                        signal.alarm(0)

                    t1 = time()

                ms = (t1 - t0) * 1000
                data["time"] += ms
                info["time"] = ms
                info["stdout"] = fm.getvalue()

                if info["status"] == SolutionStatus.FAIL:
                    print("Unhandled exception caught:")
                    print("--- STDERR ---")
                    print(info["stderr"])

                print(f"Solution ran in: {ms:.3f}ms")

                answers = get_answers(year, day_s)
                if info["status"] == SolutionStatus.TIMEOUT:
                    pass
                elif answers is None:
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
            case SolutionStatus.TIMEOUT:
                print(f"{Colour.FAIL}TIMEOUT{Colour.RESET}")

        info["logs"] = f.getvalue()
        data["tests"][day] = info
    
    summary(args, data)

    return data


def header(args):
    print(f"Advent of Code {args.year} Benchmark")
    print(f"timeout={args.timeout}")
    print(f"execution-attempts={args.attempts}")
    print()


def summary(args, data: dict):
    ...


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser(description=f"Advent of Code Benchmarker")
    parser.add_argument("year", help="The year to test and benchmark")
    parser.add_argument("--timeout", type=int, default=60,
                        help="The seconds to terminate after if solution not reached. default: 60")
    parser.add_argument("--attempts", "-n", type=int, default=1,
                        help="The number of runs of each day to average the times over")
    args = parser.parse_args()

    benchmark(args)
