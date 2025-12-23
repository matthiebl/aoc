"""
--- Day 9: Movie Theater ---
https://adventofcode.com/2025/day/9
"""

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
        return 0

    def save_as_image(self):
        scale = 100
        img = Image.new("RGB", (100_000 // scale, 100_000 // scale), "white")
        draw = ImageDraw.Draw(img)
        coords = [(x // scale, y // scale) for x, y in self.store.corners + [self.store.corners[0]]]
        draw.line(coords, fill=(0, 255, 0), width=1)

        path = self.solution_dir.joinpath("day_09_image.png")
        img.save(path)
