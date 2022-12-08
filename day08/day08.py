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
visible = np.ones(puzzle.shape)
for i in range(1, puzzle.shape[0] - 1):
    for j in range(1, puzzle.shape[1] - 1):
        left = puzzle[i, :j].max() < puzzle[i, j]
        right = puzzle[i, j + 1 :].max() < puzzle[i, j]
        top = puzzle[:i, j].max() < puzzle[i, j]
        bottom = puzzle[i + 1 :, j].max() < puzzle[i, j]
        visible[i, j] = left or right or top or bottom


# %%
print(visible.sum())
