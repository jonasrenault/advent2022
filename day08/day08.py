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
# # Day 8

# %% [markdown]
# ### Part 1

# %%
# Read puzzle input
with open("input.txt", "r") as f:
    puzzle = f.readlines()


# %%
import numpy as np

puzzle = np.array([[int(c) for c in l.strip()] for l in puzzle])


# %%
def compute_visible(puzzle: np.ndarray) -> np.ndarray:
    """
    For each cell in the matrix, compute whether it is visible
    from either top, bottom, left or right.

    Parameters
    ----------
    puzzle : np.ndarray
        the input matrix

    Returns
    -------
    np.ndarray
        a bool np.darray of shape equal to puzzle.
    """
    visible = np.ones(puzzle.shape)
    for i in range(1, puzzle.shape[0] - 1):
        for j in range(1, puzzle.shape[1] - 1):
            left = puzzle[i, :j].max() < puzzle[i, j]
            right = puzzle[i, j + 1 :].max() < puzzle[i, j]
            top = puzzle[:i, j].max() < puzzle[i, j]
            bottom = puzzle[i + 1 :, j].max() < puzzle[i, j]
            visible[i, j] = left or right or top or bottom
    return visible


# %%
print(int(compute_visible(puzzle).sum()))

# %% [markdown]
# ### Part 2

# %%
def compute_viewing(puzzle: np.ndarray) -> np.ndarray:
    """
    Compute the viewing distance for each cell in the puzzle array.

    Parameters
    ----------
    puzzle : np.ndarray
        the input array

    Returns
    -------
    np.ndarray
        an array of shape equal to puzzle's shape and with viewing distances
    """
    viewing = np.zeros(puzzle.shape)
    for i in range(1, puzzle.shape[0] - 1):
        for j in range(1, puzzle.shape[1] - 1):
            left = puzzle[i, :j] >= puzzle[i, j]
            left = 1 + np.argmax(left[::-1]) if np.any(left) else len(left)
            right = puzzle[i, j + 1 :] >= puzzle[i, j]
            right = 1 + np.argmax(right) if np.any(right) else len(right)
            top = puzzle[:i, j] >= puzzle[i, j]
            top = 1 + np.argmax(top[::-1]) if np.any(top) else len(top)
            bottom = puzzle[i + 1 :, j] >= puzzle[i, j]
            bottom = 1 + np.argmax(bottom) if np.any(bottom) else len(bottom)
            viewing[i, j] = left * right * top * bottom
    return viewing


# %%
print(int(np.max(compute_viewing(puzzle))))
