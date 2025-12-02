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
