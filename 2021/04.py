#!/usr/bin/env python3.12

import aocutils as u
from sys import argv

import numpy as np


def mark_board(board, call):
    board[board == call] = -1


def has_won(board):
    if any(np.sum(board, axis=0) == -5):
        return True
    if any(np.sum(board, axis=1) == -5):
        return True
    return False


def score(board, called):
    return np.sum((board != -1) * board) * called


def main(file: str) -> None:
    print('Day 04')

    [[called], *boards] = u.input_from_grouped_lines(file)
    called = u.map_int(called.split(','))

    boards = [np.array([u.find_digits(row) for row in board]) for board in boards]

    scores = []
    for call in called:
        [mark_board(board, call) for board in boards]
        next_boards = []
        for board in boards:
            if has_won(board):
                scores.append(score(board, call))
            else:
                next_boards.append(board)
        boards = next_boards

    p1 = scores[0]
    p2 = scores[-1]
    print(f'{p1=}')
    print(f'{p2=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '04.in'
    main(file)
