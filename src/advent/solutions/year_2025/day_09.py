"""
--- Day 9: Movie Theater ---
https://adventofcode.com/2025/day/9
"""

from functools import cmp_to_key

from PIL import Image, ImageDraw

from advent.core import Solver


class Day09(Solver):
    """Solution for day 9."""

    def prepare(self):
        self.store.corners = list(map(tuple, self.utils.chunks(self.input.nums())))

    def part1(self) -> int:
        """Solve part 1."""
        largest = 0
        for i, (x1, y1) in enumerate(self.store.corners):
            for x2, y2 in self.store.corners[i + 1 :]:
                x_diff = abs(x1 - x2) + 1
                y_diff = abs(y1 - y2) + 1
                largest = max(largest, x_diff * y_diff)
        return largest

    def part2(self) -> int:
        """Solve part 2."""
        above = [(x, y) for x, y in self.store.corners if y > 50_000]
        below = [(x, y) for x, y in self.store.corners if y < 50_000]

        rectangles = []
        for i, (x1, y1) in enumerate(above):
            for x2, y2 in above[i + 1 :]:
                rectangles.append((x1, y1, x2, y2))
        for i, (x1, y1) in enumerate(below):
            for x2, y2 in below[i + 1 :]:
                rectangles.append((x1, y1, x2, y2))
        rectangles.sort(key=self.cmp_rectangles)

        for r in rectangles:
            if self.contains_n_points(*r):
                continue
            return self.area(*r)
        return -1

    @staticmethod
    @cmp_to_key
    def cmp_rectangles(r1, r2):
        size1 = Day09.area(*r1)
        size2 = Day09.area(*r2)
        return size2 - size1

    @staticmethod
    def area(x1: int, y1: int, x2: int, y2: int) -> int:
        x_diff = abs(x1 - x2) + 1
        y_diff = abs(y1 - y2) + 1
        return x_diff * y_diff

    @staticmethod
    def order_args(a: int, b: int) -> tuple[int, int]:
        if a > b:
            return b, a
        return a, b

    def contains_n_points(self, x1: int, y1: int, x2: int, y2: int, n: int = 1) -> bool:
        x1, x2 = self.order_args(x1, x2)
        y1, y2 = self.order_args(y1, y2)

        within = 0
        for x, y in self.store.corners:
            if within >= n:
                break
            if x1 < x < x2 and y1 < y < y2:
                within += 1
        return within >= n

    def save_as_image(
        self,
        points: list | None = None,
        square: tuple | None = None,
        file_name: str = "day_09_image.png",
    ):
        if points is None:
            points = self.store.corners
        points.append(points[0])

        scale = 100
        img = Image.new("RGB", (100_000 // scale, 100_000 // scale), "white")
        draw = ImageDraw.Draw(img)

        if square is not None:
            x1, y1, x2, y2 = square
            x1, x2 = self.order_args(x1, x2)
            y1, y2 = self.order_args(y1, y2)
            draw.rectangle(
                [(x1 // scale, y1 // scale), (x2 // scale, y2 // scale)],
                fill="red",
                outline="black",
            )

        coords = [(x // scale, y // scale) for x, y in points]
        draw.line(coords, fill="green", width=1)

        path = self.solution_dir.joinpath(file_name)
        img.save(path)
