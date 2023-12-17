#!/usr/bin/env python3.12

import aocutils as u
from sys import argv
import heapq as hq

"""
In the end, kind of happy with this solution. Even though it took way too long.

I had an alternate solution previously, but did not cache, and handled
skipping wrong directions more complicated than necessary.
"""

DX = [0, 1, 0, -1]
DY = [-1, 0, 1, 0]


def main(file: str) -> None:
    print('Day 17')

    lava = u.input_as_lines(file)

    H = len(lava)
    W = len(lava[0])
    target = (W-1, H-1)

    def dijkstra(min_steps, max_steps):
        dist = u.defaultdict(lambda: float('inf'))
        # dist is (x, y, dir to coord, # of steps in that dir): sum of heat loss
        dist[0, 0, 0, 0] = 0
        q = [(0, 0, 0, None, 0)]
        while q:
            heat_loss, x, y, dir, steps = hq.heappop(q)
            if (x, y) == target:
                return heat_loss

            for d in range(4):
                if d == dir and steps >= max_steps:
                    continue
                if dir is not None and d != dir and steps < min_steps:
                    continue
                if ((d + 2) % 4) == dir:
                    continue
                nx = x + DX[d]
                ny = y + DY[d]
                if 0 <= nx < W and 0 <= ny < H:
                    score = heat_loss + int(lava[ny][nx])
                    nprev = steps + 1 if d == dir else 1
                    if score < dist[nx, ny, d, nprev]:
                        dist[nx, ny, d, nprev] = score
                        hq.heappush(
                            q, (score, nx, ny, d, nprev))

    p1 = dijkstra(1, 3)
    print(f'{p1=}')
    p2 = dijkstra(4, 10)
    print(f'{p2=}')


if __name__ == '__main__':
    file = argv[1] if len(argv) >= 2 else '17.in'
    main(file)
