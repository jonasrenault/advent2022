# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.14.1
#   kernelspec:
#     display_name: Python 3.10.8 ('advent')
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Day 12

# %% [markdown]
# ### Part 1

# %%
# Read puzzle input
with open("input.txt", "r") as f:
    puzzle = f.readlines()


# %%
import numpy as np

puzzle = [[ord(c) for c in l.strip()] for l in puzzle]
puzzle = np.array(puzzle)
start = tuple(np.argwhere(puzzle == ord("S"))[0])
end = tuple(np.argwhere(puzzle == ord("E"))[0])
puzzle[start] = ord("a")
puzzle[end] = ord("z")

# %%
from typing import Tuple, List, Callable

dirs = {(1, 0), (0, 1), (-1, 0), (0, -1)}


def get_neighbors(
    pos: Tuple[int, int],
    puzzle: np.ndarray,
    visited: np.ndarray,
    height_cond: Callable[[int, int], bool],
) -> List[Tuple[int, int]]:
    """
    Get the possible neighbors for pos, given the heights matrix and the matrix
    of already visited positions.

    Parameters
    ----------
    pos : Tuple[int, int]
        the position to get neighbors for
    puzzle : np.ndarray
        the heights matrix
    visited : np.ndarray
        the matrix of already visited positions
    height_cond : Callable[[int, int], bool]
        callback condition to decide if moving to neighbor is possible

    Returns
    -------
    List[Tuple[int, int]]
        the list of possible neighbors
    """
    neighbors = []
    for d in dirs:
        neighbor = (pos[0] + d[0], pos[1] + d[1])
        if (
            0 <= neighbor[0] < puzzle.shape[0]
            and 0 <= neighbor[1] < puzzle.shape[1]
            and not visited[neighbor]
            and height_cond(puzzle[pos], puzzle[neighbor])
        ):
            neighbors.append(neighbor)

    return neighbors


# %%
def dijkstra(
    puzzle: np.ndarray, start: Tuple[int, int], height_cond: Callable[[int, int], bool]
) -> np.ndarray:
    """
    Compute the minimum cost to reach each position in the puzzle from the
    start node.

    Parameters
    ----------
    puzzle : np.ndarray
        the heights of each position
    start : Tuple[int, int]
        the starting indices
    height_cond : Callable[[int, int], bool]
        callback condition to decide if moving to neighbor is possible

    Returns
    -------
    np.ndarray
        the cost matrix
    """
    visited = np.zeros(puzzle.shape, dtype=bool)
    costs = np.full(puzzle.shape, puzzle.size)
    costs[start] = 0

    while not visited.all():
        pos = tuple(
            min(np.argwhere(visited == False).tolist(), key=lambda x: costs[tuple(x)])
        )
        visited[pos] = True
        neighbors = get_neighbors(pos, puzzle, visited, height_cond)
        for neighbor in neighbors:
            if costs[pos] + 1 < costs[neighbor]:
                costs[neighbor] = costs[pos] + 1

    return costs


# %%
# only move to neighbors with height lower than current height + 1
condition = lambda height1, height2: height2 <= height1 + 1
costs = dijkstra(puzzle, start, condition)
print(costs[end])

# %% [markdown]
# ### Part 2

# %%
# inverse the condition and start from the end
inv_condition = lambda height1, height2: height1 <= height2 + 1
costs = dijkstra(puzzle, end, inv_condition)
print(costs[puzzle == ord("a")].min())
