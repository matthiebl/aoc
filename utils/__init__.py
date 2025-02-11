from .graph_utils import (  # pre-made searches; quick input parsing; handle grids; utilities
    bfs, create_grid, dfs, dijkstras, directions, enumerate_grid, find_in_grid,
    grid_to_graph, is_end_pos, neighbours, show_grid, weight_const,
    weight_of_pos, within_grid)
from .input_handling import get_input, parse_args
from .interpreters import Interpreter
from .types.list import CircularList
from .wrappers import echo, memoize


def import_day(package: str, attribute=None):
    from contextlib import redirect_stdout
    from importlib import import_module
    from io import StringIO
    f = StringIO()
    with redirect_stdout(f):
        module = import_module(package)
    return getattr(module, attribute) if attribute else module


def flatmap(lst: list[list]):
    return [item for list in lst for item in list]


def nums(s: str):
    """Parse the input for all positive or negative integers."""
    from re import findall

    return map(int, findall(r"(-?\d+)", s))


def chunks(it, n: int = 2, excess_ok: bool = False):
    """A generator that returns chunks of size `n` from the iterable."""
    it = iter(it)
    try:
        tmp = []
        while True:
            for _ in range(n):
                tmp.append(next(it))
            yield tmp
            tmp = []
    except StopIteration:
        if tmp and excess_ok:
            yield tmp


def windows(it, n: int = 2):
    """A generator that returns the windows of size `n` from the iterable."""
    window = []
    for i in it:
        window.append(i)
        if len(window) == n:
            yield tuple(window)
            window.pop(0)


def mul(n: int, *ns: list[int]) -> int:
    """Multiplies all the numbers together and returns their result."""
    from functools import reduce
    if not isinstance(n, int):
        return reduce(lambda a, b: a * b, n, 1)
    res = n
    for n in ns:
        res *= n
    return res


def tuple_add(t1: tuple[int, ...], t2: tuple[int, ...]) -> tuple[int, ...]:
    """Add two tuples of the same length."""
    return tuple(a + b for a, b in zip(t1, t2))


def manhattan(r1: int, c1: int, r2: int, c2: int) -> int:
    return abs(r1 - r2) + abs(c1 - c2)


def nums_sum_to(target: int, n: int = 2) -> list[tuple[int]]:
    """Find all the combinations of `n` positive numbers that sum to the `target` value."""
    if n == 1:
        return [(target,)]
    ns = []
    for i in range(1, target + 1 - n + 1):
        ns += list(map(lambda t: (i,) + t, nums_sum_to(target - i, n - 1)))
    return ns


def crt(a: list[int], n: list[int]) -> int:
    """
    Finds `x` using the Chinese Remainder Theorem for list of `a`s and `n`s where

    ```
    x = a_1 % n_1
    x = a_2 % n_2
    ...
    x = a_i % n_i
    """
    N = mul(n)
    E = [N // n_i for n_i in n]
    y = [pow(e_i, n_i - 2, n_i) for e_i, n_i in zip(E, n)]
    return sum(a_i * e_i * y_i for a_i, e_i, y_i in zip(a, E, y)) % N
