from .input_handling import parse_args, get_input


def directions(request: (list | int | str) = 4) -> list[tuple]:
    """
    Return the directional `(r, c)` differences for each neighbour.

    `request` can be a list of index orders where each index is one of:
    ```
    [[0, 1, 2],
     [3, 4, 5],
     [6, 7, 8]]
    ```
    or it can be a key into the common orderings.
    """
    neighbours = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]
    common_orderings = {
        4: [1, 3, 5, 7],
        8: [0, 1, 2, 3, 5, 6, 7, 8],
        9: [0, 1, 2, 3, 4, 5, 6, 7, 8],
        "X": [0, 4, 8, 2, 4, 6],
    }
    if isinstance(request, list):
        order = request
    elif request in common_orderings:
        order = common_orderings[request]
    else:
        raise ValueError(f"No known neighbour order for {request}")
    return [neighbours[i] for i in order]


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
