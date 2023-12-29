#!/usr/bin/env python3

from re import findall
from typing import Callable, Iterable, TypeVar, Container
from ast import literal_eval
from functools import reduce

# easy imports
from collections import Counter, defaultdict

# Types
A = TypeVar('A')
B = TypeVar('B')

Coord = tuple[int, int]
Coords = list[Coord]

# Interval is tuple (lo, hi) representing mathematical interval [lo, hi)
Interval = tuple[int, int]
Intervals = list[Interval]


DX = [0, 1, 0, -1]
DY = [-1, 0, 1, 0]
DXY = list(zip(DX, DY))


"""
Input Parsing
"""


def read_input(file: str) -> str:
    return open(file, 'r').read()


def input_as_lines(file: str, map: Callable[[str], A] = str) -> list[A]:
    return [map(line) for line in read_input(file).split('\n')]


def input_from_grouped_lines(file: str, map: Callable[[str], A] = str) -> list[list[A]]:
    return [[map(line) for line in group.split('\n')] for group in read_input(file).split('\n\n')]


def double_sep(
    s: str,
    sep1: str,
    sep2: str,
    map: Callable[[str], A] = str,
    group: Callable[[list[A]], B] = list
) -> list[list[A]]:
    return list(group(map(b) for b in a.split(sep2)) for a in s.split(sep1))


def map_int(it: Iterable[str]) -> list[int]:
    return list(map(int, it))


def mul(it: Iterable[int]) -> int:
    return reduce(lambda x, acc: x * acc, it, 1)


def find_digits(s: str, map: Callable[[str], A] = int, group: Callable[[str], B] = list) -> 'B[A]':
    return group(map(digit) for digit in findall(r'(-?[0-9]+)', s))


def list_eval(s: str) -> list:
    return literal_eval(s)


"""
Grouping data
"""


def groups_of(it: Iterable[A], by: int) -> list[Iterable[A]]:
    return [it[i:i + by] for i in range(0, len(it), by)]


def columns(l: list[A]) -> list[tuple[A]]:
    return list(zip(*l))


"""
Min maxing
"""


def sum_max(amount: int, it: Iterable[int], key: Callable[[int], int] = int) -> int:
    it = sorted(it, key=key)
    return sum(it[-min(amount, len(it)):])


def min_max_x_y(it: Iterable[tuple[int, int]]) -> tuple[int, int, int, int]:
    min_x = min(x for x, y in it)
    min_y = min(y for x, y in it)
    max_x = max(x for x, y in it)
    max_y = max(y for x, y in it)
    return (min_x, min_y, max_x, max_y)


def manhattan_dist(x1: int, y1: int, x2: int, y2: int) -> int:
    return abs(x1 - x2) + abs(y1 - y2)


"""
Tuple utils
"""


def add_tup(left: tuple[int], right: tuple[int]) -> tuple:
    return tuple(l + r for l, r in zip(left, right))


def mul_tup(tup: tuple[int], mulitplier: int) -> tuple:
    return tuple(x * mulitplier for x in tup)


def range_overlap(range: Interval, mask: Interval) -> tuple[Interval, Interval, Interval]:
    """
    range is a tuple that represents the range [a, b)
    mask  is a tuple that represents the range [c, d)

    casts a shadow from range, over mask, and
    finds the ranges, before, in between and after
    that correspend the the parts of the shadow
    if that makes any sense

    a --------------- b
            c --------------- d
    |        |       |
    [before ][middle][after ]
    """
    a, b = range
    c, d = mask

    before = (a, min(b, c))
    middle = (max(a, c), min(b, d))
    after = (max(a, d), b)

    if before[0] >= before[1]:
        before = None
    if middle[0] >= middle[1]:
        middle = None
    if after[0] >= after[1]:
        after = None

    return before, middle, after


def merge_intervals(intervals: Interval) -> Interval:
    intervals.sort()
    if len(intervals) == 0:
        return []

    merged = [intervals[0]]

    for lo, hi in intervals[1:]:
        mlo, mhi = merged[-1]
        if lo > mhi:
            merged.append((lo, hi))
        elif lo <= mhi:
            merged[-1] = (mlo, max(hi, mhi))

    return merged


"""
Array utils
"""


def in_grid(grid: list[list[A]], row: int, col: int) -> bool:
    """row = y, col = x"""
    return 0 <= row < len(grid) and 0 <= col < len(grid[row])


"""
Array creation and display
"""


def array_2D(base: A, width: int, height: int) -> list[list[A]]:
    return [[base] * width for _ in range(height)]


def array_3D(base: A, x: int, y: int, z: int) -> list[list[list[A]]]:
    return [array_2D(base, x, y) for _ in range(z)]


def array_collect_def(it: Iterable[tuple[int, int]], fill: str = '#', empty: str = '.') -> list[list[str]]:
    if list(it) == []:
        it = [(0, 0)]
    return array_collect(it, min_max_x_y(it), fill, empty)


def array_collect(it: Iterable[tuple[int, int]], mmxy: tuple[int, int, int, int], fill: str = '#', empty: str = '.') -> list[list[str]]:
    x1, y1, x2, y2 = mmxy
    array = array_2D(empty, x2 - x1 + 1, y2 - y1 + 1)
    for x, y in it:
        array[y - y1][x - x1] = fill
    return array


def map_collect(dic: dict[tuple[int, int], str], empty: str = ' ') -> list[list[str]]:
    x1, y1, x2, y2 = min_max_x_y([k for k in dic])
    array = array_2D(empty, x2 - x1 + 1, y2 - y1 + 1)
    for (x, y), t in dic.items():
        array[y - y1][x - x1] = t
    return array


def array_visualise(arr: list[list[str]], sep: str = '') -> None:
    for row in arr:
        print(sep.join(row))
    print()


def visualise(it: Iterable[tuple[int, int]], fill: str = '#', empty: str = '.', sep: str = ''):
    array_visualise(array_collect_def(it, fill, empty), sep)


def dict_visualise(d: dict, name: str, indent: int = 0):
    tabs = '  ' * indent
    print(tabs + str(name) + ': {')
    for k, v in d.items():
        if isinstance(v, dict):
            dict_visualise(v, k, indent + 1)
        else:
            print(tabs + '  ' + str(k) + ': ' + str(v) + ',')
    print(tabs + '}' + (',' if indent > 0 else ''))


"""
Graph utils
"""


def graph_from_grid(grid: list[list[A]], valid: list[A]) -> dict[Coord, list[Coord]]:
    G: dict[Coord, list[Coord]] = {}
    for y, row in enumerate(grid):
        for x, ch in enumerate(row):
            if ch not in valid:
                continue
            G[(x, y)] = []
            for dx, dy in DXY:
                if in_grid(grid, y + dy, x + dx) and grid[y + dy][x + dx] in valid:
                    G[(x, y)].append((x + dx, y + dy))
    return G
