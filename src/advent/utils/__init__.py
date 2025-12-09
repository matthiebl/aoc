from typing import Iterable


class Utils:
    @staticmethod
    def chunks(it, n: int = 2, exact: bool = True):
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
            if tmp and not exact:
                yield tmp

    @staticmethod
    def windows(it, n: int = 2):
        """A generator that returns the windows of size `n` from the iterable."""
        window = []
        for i in it:
            window.append(i)
            if len(window) == n:
                yield tuple(window)
                window.pop(0)

    @staticmethod
    def euclidean_distance(a: Iterable[int], b: Iterable[int] = None, relative: bool = False):
        """Returns the euclidean (direct point to point) distance of the two iterables `a` and `b`
        of arbitrary dimensions.

        If `b` is not provided, it is assumed to take the distance from the origin `(0, 0, ...)`.

        Args:
            a (Iterable[int]): Point A
            b (Iterable[int], optional): Point B. Defaults to origin (0, 0).
            relative (bool, optional): If actual distance not needed, skips sqrt operation. Defaults to False.

        Returns:
            int: The distance between two points in space.
        """
        if b is None:
            from itertools import repeat

            b = repeat(0)

        summation = sum((n1 - n2) ** 2 for n1, n2 in zip(a, b))
        if relative:
            return summation
        from math import sqrt

        return sqrt(summation)
