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
# # Day 9

# %% [markdown]
# ### Part 1

# %%
# Read puzzle input
with open("input.txt", "r") as f:
    puzzle = f.readlines()


# %%
puzzle = [tuple(l.strip().split(" ")) for l in puzzle]

dirs = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}

# %%
from typing import Tuple, MutableSet


def step(
    H: Tuple[int, int],
    T: Tuple[int, int],
    s: Tuple[str, str],
    positions: MutableSet[Tuple[int, int]],
):
    d, u = s
    for _ in range(int(u)):
        new_H = (H[0] + dirs[d][0], H[1] + dirs[d][1])
        if abs(new_H[0] - T[0]) > 1 or abs(new_H[1] - T[1]) > 1:
            T = H
            positions.add(T)
        H = new_H
    return H, T


# %%
H = (0, 0)
T = (0, 0)
positions = set()
positions.add((0, 0))
for s in puzzle:
    H, T = step(H, T, s, positions)

# %%
print(len(positions))

# %% [markdown]
# ### Part 2

# %%
from typing import List
import numpy as np


def step_knots(
    knots: List[np.ndarray],
    s: Tuple[str, str],
    positions: MutableSet[Tuple[int, int]],
):
    d, u = s
    for _ in range(int(u)):
        # move head in dir
        knots[0] = knots[0] + np.array(dirs[d])
        moved = True
        i = 1
        while moved and i < 10:
            # for each knot, move it in direction of knot before it
            # if it is not touching it
            diff = knots[i - 1] - knots[i]
            if diff.max() > 1 or diff.min() < -1:
                knots[i] = knots[i] + diff.clip(-1, 1)
                i += 1
            else:
                moved = False
            if i == 10:
                positions.add(tuple(knots[i - 1]))


# %%
knots = [np.array((0, 0)) for _ in range(10)]
positions = set()
positions.add((0, 0))
for s in puzzle:
    step_knots(knots, s, positions)

# %%
print(len(positions))
