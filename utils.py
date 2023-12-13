#!/usr/bin/env python3

from sys import argv
from os import chmod, path
from re import findall
from aocd import get_data
from typing import Callable, Iterable
from ast import literal_eval

A = any
B = any


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
    group: Callable[[list], B] = list
) -> list['B[A]']:
    return [group(map(b) for b in a.split(sep2)) for a in s.split(sep1)]


def map_int(it: Iterable[str]) -> list[int]:
    return list(map(int, it))


def find_digits(s: str, map: Callable[[str], A] = int, group: Callable[[str], B] = list) -> 'B[A]':
    return group(map(digit) for digit in findall(r'(-?[0-9]+)', s))


def list_eval(s: str) -> list:
    return literal_eval(s)


"""
Grouping data
"""


def groups_of(it: Iterable[A], by: int) -> list[Iterable[A]]:
    return [it[i:i + by] for i in range(0, len(it), by)]


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


"""
Tuple utils
"""


def add_tup(left: tuple, right: tuple) -> tuple:
    return tuple(l + r for l, r in zip(left, right))


def range_overlap(range: tuple[int, int], mask: tuple[int, int]) -> tuple[tuple[int, int], tuple[int, int], tuple[int, int]]:
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


def dict_visualise(d: dict, name: str, indent: int = 0):
    tabs = '  ' * indent
    print(tabs + name + ': {')
    for k, v in d.items():
        if isinstance(v, dict):
            dict_visualise(v, k, indent + 1)
        else:
            print(tabs + '  ' + str(k) + ': ' + str(v) + ',')
    print(tabs + '}' + (',' if indent > 0 else ''))


"""
Creation of script and input
"""


def create_input(day: str, year: int) -> None:
    with open(f'{day}.in', 'w') as f:
        f.write(get_data(day=int(day), year=year))


def create_script(day: str) -> None:
    if path.exists(f'{day}.py') and input(f'{day}.py already exists. Are you sure you want to overwrite? ') != 'y':
        return
    with open(f'{day}.py', 'w') as f:
        f.write(
            f"""#!/usr/bin/env python3.12

import aocutils as u
from sys import argv

def main(file: str) -> None:
    print('Day {day}')

    data = u.input_as_lines(file)
    print(data)

if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '{day}.in'
    main(file)
""")
    chmod(f'{day}.py', 0o744)


if __name__ == '__main__':

    if len(argv) != 4 or argv[1] not in ['script', 'input', 'setup'] or not argv[2].isdigit() or not argv[3].isdigit():
        print(f'Usage: \'{argv[0]} [command] <year> <day>')
        exit(1)
    command = argv[1]
    year = int(argv[2])
    day = argv[3]

    if command == 'script':
        create_script(day)
    elif command == 'input':
        create_input(day, year)
    elif command == 'setup':
        create_script(day)
        create_input(day, year)
