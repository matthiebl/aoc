#!/usr/bin/env python3.12

import json
from sys import argv

import aocutils as u


def json_sum(json) -> int:
    if isinstance(json, int):
        return json
    if isinstance(json, str):
        return 0
    if isinstance(json, list):
        return sum(json_sum(it) for it in json)
    return sum(json_sum(v) for v in json.values())


def json_sum_p2(json) -> int:
    if isinstance(json, int):
        return json
    if isinstance(json, str):
        return 0
    if isinstance(json, list):
        return sum(json_sum_p2(it) for it in json)
    return sum(json_sum_p2(v) for v in json.values() if not is_property_within(json))


def is_property_within(json, property='red'):
    if isinstance(json, int):
        return False
    if isinstance(json, str):
        return False
    if isinstance(json, list):
        return False
    if any(v == property for v in json.values()):
        return True
    return False


def main(file: str) -> None:
    print('Day 12')

    data = u.read_input(file)

    j = json.loads(data)
    p1 = json_sum(j)
    print(f'{p1=}')

    p2 = json_sum_p2(j)
    print(f'{p2=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '12.in'
    main(file)
