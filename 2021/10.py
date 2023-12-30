#!/usr/bin/env python3.12

import aocutils as u
from sys import argv

import heapq as hq

matches = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}

syntax_error = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

auto_complete = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4,
}


def main(file: str) -> None:
    print('Day 10')

    bracket_data = u.input_as_lines(file)

    p1 = 0
    auto_complete_scores = []
    for brackets in bracket_data:
        stack = []
        for b in brackets:
            if b in '([<{':
                stack.append(b)
                continue
            bb = stack.pop()
            if matches[bb] == b:
                continue
            p1 += syntax_error[b]
        auto_score = 0
        while stack:
            b = stack.pop()
            auto_score = auto_score * 5 + auto_complete[b]
        hq.heappush(auto_complete_scores, auto_score)

    print(f'{p1=}')

    for _ in range(len(auto_complete_scores) // 2 + 1):
        hq.heappop(auto_complete_scores)

    p2 = hq.heappop(auto_complete_scores)
    print(f'{p2=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '10.in'
    main(file)
