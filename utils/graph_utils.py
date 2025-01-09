"""BFS"""


def bfs(graph: dict, start, is_end, initial_dist: int = 0) -> tuple:
    """
    ### Breadth First Search

    Provided a graph in the form `{ A: [(w, B), ...] }` we check
    if we have reached a goal position in `is_end(A): bool`

    Returns the goal position (or `None` if none found) and the visited set

    Weight of each adjacent cell is ignored
    """
    from collections import deque

    visited = set()
    queue = deque([(initial_dist, start)])
    while queue:
        d, nxt = queue.popleft()
        if nxt in visited:
            continue
        visited.add(nxt)

        if is_end(nxt):
            return d, visited

        queue.extend([(d + w, pos) for w, pos in graph[nxt]])

    return None, visited


"""DFS"""


def dfs(graph: dict, start, is_end, initial_dist: int = 0):
    """
    ### Depth First Search

    Provided a graph in the form `{ A: [(w, B), ...] }` we check
    if we have reached a goal position in `is_end(A): bool`

    Returns the goal position (or `None` if none found) and the visited set

    Weight of each adjacent cell is ignored
    """
    visited = set()
    stack = [(initial_dist, start)]
    while stack:
        d, nxt = stack.pop()
        if nxt in visited:
            continue
        visited.add(nxt)

        if is_end(nxt):
            return nxt, visited

        stack.extend([(d + w, pos) for w, pos in graph[nxt]])

    return None, visited


"""DIJKSTRA"""


def dijkstras(graph: dict, start, is_end, initial_dist: int = 0) -> tuple[int | None, dict]:
    """
    ### Dijkstras Shortest Path

    Provided a graph in the form `{ A: [(w, B), ...] }` we check
    if we have reached a goal position in `is_end(A): bool` If we do find
    a goal, we return the distance to that position.

    Returns the distance to `is_end` if found; otherwise the distance mapping
    """
    from heapq import heapify, heappush, heappop

    distances = {pos: float("inf") for pos in graph}
    distances[start] = initial_dist

    visited = set()

    heap = [(initial_dist, start)]
    heapify(heap)

    while heap:
        d, nxt = heappop(heap)
        if nxt in visited:
            continue
        visited.add(nxt)

        if is_end(nxt):
            return d, distances

        for w, adj in graph[nxt]:
            tentative = d + w
            if tentative < distances[adj]:
                distances[adj] = tentative
                heappush(heap, (tentative, adj))

    return None, distances


"""Utilities"""


def show_grid(grid: list[list]):
    for row in grid:
        print("".join(row))


def weight_const(val: int = 1):
    """Utility for `grid_to_graph` that provides a function that always returns `val`."""
    def weight(grid, pos, adj):
        return val
    return weight


def weight_of_pos(grid: list[list], pos: tuple, adj: tuple):
    """Utility for `grid_to_graph` that provides the value of the adjacent position as the weight."""
    r, c = adj
    return int(grid[r][c])


def is_end_pos(r: int, c: int):
    """Utility for checking is_end with a row and column value."""
    def is_end(pos):
        return pos[0] == r and pos[1] == c
    return is_end


def grid_to_graph(grid: list[list],
                  adjacent_request: list | int | str = 4,
                  weight=weight_const(),
                  valid_tiles: str = None):
    """
    Converts a grid into a weighted graph

    Takes a 2D `grid`, and returns a weighted graph in the form `{ (r, c): [(w, r, c), ...] }`

    Determines the weight of each connection via the callback `weight(grid, pos, adj) -> int`,
    by default returning constant weight of `1`

    Finds adjacent positions with `adjacent_request` being the input into `directions`. Use
    any request you can provide to `directions` or a list of index orders where indexes are:
    ```
    [[0, 1, 2],
     [3, 4, 5],
     [6, 7, 8]]
    ```
    """
    graph: dict[tuple, list[tuple]] = {}
    for (r, c), val, _ in enumerate_grid(grid):
        if valid_tiles and val not in valid_tiles:
            continue
        graph[(r, c)] = []
        for dr, dc in directions(adjacent_request):
            if within_grid(grid, r + dr, c + dc):
                if valid_tiles and grid[r + dr][c + dc] not in valid_tiles:
                    continue
                w = weight(grid, (r, c), (r + dr, c + dc))
                graph[(r, c)].append((w, (r + dr, c + dc)))
    return graph


def directions(request: (list | int | str) = 4) -> list[tuple]:
    """
    Return the directional `(r, c)` differences for each neighbour.

    `request` can be a list of index orders where each index is one of:
    ```
    [[0, 1, 2],
     [3, 4, 5],
     [6, 7, 8]]
    ```
    or it can be a key into the common orderings.
    """
    neighbours = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]
    common_orderings = {
        4: [1, 3, 5, 7],
        8: [0, 1, 2, 3, 5, 6, 7, 8],
        9: [0, 1, 2, 3, 4, 5, 6, 7, 8],
        "X": [0, 4, 8, 2, 4, 6],
        "cw4": [1, 5, 7, 3],
        "cw8": [0, 1, 2, 5, 8, 7, 6, 3]
    }
    if isinstance(request, list):
        order = request
    elif request in common_orderings:
        order = common_orderings[request]
    else:
        raise ValueError(f"No known neighbour order for {request}")
    return [neighbours[i] for i in order]


def within_grid(grid: list[list], r: int, c: int) -> bool:
    return 0 <= r < len(grid) and 0 <= c < len(grid[0])


def neighbours(grid: list[list], r: int, c: int, request=4):
    """Piggy-backs the `directions` request format to provide the new row and column and grid value."""
    for dr, dc in directions(request):
        if within_grid(grid, r + dr, c + dc):
            yield (r + dr, c + dc), grid[r + dr][c + dc]


def enumerate_grid(grid: list[list], skip: str = ""):
    for r, row in enumerate(grid):
        for c, val in enumerate(row):
            if val not in skip:
                yield (r, c), val, row


def find_in_grid(grid: list[list[str]], search: str):
    for (r, c), val, _ in enumerate_grid(grid):
        if val in search:
            yield (r, c)


def create_grid(r: int, c: int, fill: str = ".", blocks: list[tuple[int, int, str]] = []):
    """
    Create a grid of `r` rows and `c` columns filled with `fill` or `.` by default.

    Also place `(r, c, v)` items down where `v` is some string value to place.
    """
    grid = [[fill] * c for _ in range(r)]
    for br, bc, v in blocks:
        if within_grid(grid, br, bc):
            grid[br][bc] = v
    return grid
