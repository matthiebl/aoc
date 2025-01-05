from .graph_utils import (
    bfs, dfs, dijkstras,  # pre-made searches
    grid_to_graph, create_grid,  # quick input parsing
    show_grid, enumerate_grid, find_in_grid, directions, within_grid, neighbours,  # handle grids
    weight_const, weight_of_pos, is_end_pos,  # utilities
)
from .input_handling import parse_args, get_input
from .wrappers import memoize


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
            yield window
            del window[0]


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
    if n == 1:
        return [(target,)]
    ns = []
    for i in range(1, target + 1 - n + 1):
        ns += list(map(lambda t: (i,) + t, nums_sum_to(target - i, n - 1)))
    return ns
