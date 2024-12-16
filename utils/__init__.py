from .graph_utils import show_grid, grid_to_graph, weight_const, weight_of_pos, bfs, dijkstras, dfs, directions, within_grid, enumerate_grid, find_in_grid
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


def mul(*ns: list[int]) -> int:
    """Mulitplies all the numbers together and returns their result."""
    from functools import reduce
    return reduce(lambda a, b: a * b, ns, 1)


def tuple_add(t1: tuple[int, ...], t2: tuple[int, ...]) -> tuple[int, ...]:
    """Add two tuples of the same length."""
    return tuple(a + b for a, b in zip(t1, t2))
