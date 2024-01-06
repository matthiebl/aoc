#!/usr/bin/env python3.12

import aocutils as u
from sys import argv

from math import floor, ceil


class SnailNum:
    def __init__(self, left=None, right=None) -> None:
        self.val: int | None = None
        self.left: SnailNum | None = left
        self.right: SnailNum | None = right

    def from_list(self, lst: list | int):
        if type(lst) == int:
            self.val = lst
        else:
            self.left = SnailNum().from_list(lst[0])
            self.right = SnailNum().from_list(lst[1])
        return self

    def to_list(self):
        if self.val is not None:
            return self.val
        return [self.left.to_list(), self.right.to_list()]

    def size(self, t):
        if t is None:
            return 0
        if t.left is None and t.right is None:
            return 1
        l = self.size(t.left)
        r = self.size(t.right)
        return 1 + l + r

    def index_add(self, sn, index, value):
        if sn is None:
            return None
        curr = self.size(sn.left)
        if index == curr:
            self.val += value
        elif index < curr and self.left:
            self.left.index_add(sn.left, index, value)
        elif index > curr and self.right:
            self.right.index_add(sn.right, index - (curr + 1), value)
        return self

    def explode(self, root, index: int, depth: int = 0) -> bool:
        if self.left is not None and self.left.explode(root, index - 1 - self.size(self.left.left), depth + 1):
            return True

        if self.left and self.right and type(self.left.val) == int and type(self.right.val) == int and depth >= 4:
            root.index_add(root, index - 1, self.left.val)
            root.index_add(root, index, self.right.val)
            self.left = None
            self.right = None
            self.val = 0
            return True

        if self.right is not None and self.right.explode(root, index + 1 + self.size(self.right.left), depth + 1):
            return True
        return False

    def split(self) -> bool:
        if self.left is not None and self.left.split():
            return True

        if self.val is not None and self.val > 9:
            self.left = SnailNum().from_list(floor(self.val / 2))
            self.right = SnailNum().from_list(ceil(self.val / 2))
            self.val = None
            return True

        if self.right is not None and self.right.split():
            return True
        return False

    def reduce(self):
        while True:
            print('\t', self.to_list())
            if self.explode(self, self.size(self.left)):
                print('explode')
                continue
            if self.split():
                print('split')
                continue
            print('done')
            break
        return self

    def magnitude(self):
        if self.val is not None:
            return self.val
        return 3 * self.left.magnitude() + 2 * self.right.magnitude()


class SFNumber:
    def __init__(self) -> None:
        self.list = ''

    def from_list(self, list_form: list):
        self.list = list_form
        return self

    def from_string(self, string_form: str):
        self.list = self._from_string(string_form)
        return self

    def _from_string(self, string_form: str) -> list:
        if string_form == '':
            return []
        if string_form[0] in '[]':
            return [string_form[0], *self._from_string(string_form[1:])]
        if string_form[0] in ',':
            return self._from_string(string_form[1:])
        i = 0
        while string_form[i].isdigit():
            i += 1
        return [int(string_form[:i]), *self._from_string(string_form[i:])]

    def __add__(self, other):
        return SFNumber().from_list(['[', *self.list, *other.list, ']'])

    def _explode(self) -> bool:
        depth = 0
        for i, c in enumerate(self.list):
            if c == '[':
                depth += 1
            elif c == ']':
                depth -= 1
            elif depth > 4 and type(c) == int and type(self.list[i+1]) == int:
                left, right = c, self.list[i+1]
                for j in range(i - 1, 0, -1):
                    if type(self.list[j]) == int:
                        self.list[j] += left
                        break
                for j in range(i + 2, len(self.list)):
                    if type(self.list[j]) == int:
                        self.list[j] += right
                        break
                for _ in range(4):
                    self.list.pop(i - 1)
                self.list.insert(i - 1, 0)
                return True
        return False

    def _split(self) -> bool:
        for i, c in enumerate(self.list):
            if type(c) == int and c >= 10:
                self.list = self.list[:i] + ['[', floor(c / 2), ceil(c / 2), ']'] + self.list[i + 1:]
                return True
        return False

    def reduce(self) -> None:
        while True:
            if self._explode():
                continue
            elif self._split():
                continue
            else:
                break
        return self

    def _str(self, l: list) -> str:
        if len(l) == 0:
            return ''
        if len(l) == 1:
            return str(l[0])
        if type(l[0]) == int and l[1] != ']':
            return str(l[0]) + ',' + self._str(l[1:])
        if l[0] == ']' and l[1] != ']':
            return '],' + self._str(l[1:])
        return str(l[0]) + self._str(l[1:])

    def __str__(self) -> str:
        return self._str(self.list)

    def _magnitude(self, l: list) -> int:
        if type(l) == int:
            return l
        return 3 * self._magnitude(l[0]) + 2 * self._magnitude(l[1])

    def magnitude(self) -> int:
        string = str(self)
        lst = u.list_eval(string)
        return self._magnitude(lst)


def main(file: str) -> None:
    print('Day 18')

    raw_nums = u.input_as_lines(file)

    sn = SFNumber().from_string(raw_nums[0])
    for lst in raw_nums[1:]:
        sn2 = SFNumber().from_string(lst)
        sn = sn + sn2
        sn.reduce()
    sn.reduce()
    p1 = sn.magnitude()
    print(f'{p1=}')

    p2 = 0
    for i, raw_a in enumerate(raw_nums):
        a = SFNumber().from_string(raw_a)
        for raw_b in raw_nums[:i]:
            b = SFNumber().from_string(raw_b)
            p2 = max(p2, (a + b).reduce().magnitude())
            p2 = max(p2, (b + a).reduce().magnitude())
    print(f'{p2=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '18.in'
    main(file)
