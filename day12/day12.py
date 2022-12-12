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

# %%
from typing import Tuple, List

dirs = {(1, 0), (0, 1), (-1, 0), (0, -1)}


def get_neighbors(
    pos: Tuple[int, int], puzzle: np.ndarray, visited: np.ndarray
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
            and (puzzle[neighbor] < puzzle[pos] or puzzle[neighbor] <= puzzle[pos] + 1)
        ):
            neighbors.append(neighbor)

    return neighbors


# %%
def dijkstra(puzzle: np.ndarray, start: Tuple[int, int]) -> np.ndarray:
    """
    Compute the minimum cost to reach each position in the puzzle from the
    start node.

    Parameters
    ----------
    puzzle : np.ndarray
        the heights of each position
    start : Tuple[int, int]
        the starting indices

    Returns
    -------
    np.ndarray
        the cost matrix
    """
    visited = np.zeros(puzzle.shape, dtype=bool)
    costs = np.full(puzzle.shape, puzzle.size)
    costs[tuple(start)] = 0

    while not visited.all():
        pos = tuple(
            min(np.argwhere(visited == False).tolist(), key=lambda x: costs[tuple(x)])
        )
        visited[pos] = True
        n = get_neighbors(pos, puzzle, visited)
        for x in n:
            if costs[pos] + 1 < costs[x]:
                costs[x] = costs[pos] + 1

    return costs


# %%
start = np.argwhere(puzzle == ord("S"))[0]
end = np.argwhere(puzzle == ord("E"))[0]
input = puzzle.copy()
input[tuple(start)] = ord("a")
input[tuple(end)] = ord("z")

costs = dijkstra(input, tuple(start))
print(costs[tuple(end)])
