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
# # Day 23

# %% [markdown]
# ### Part 1

# %%
# Read puzzle input
with open("input.txt", "r") as f:
    puzzle = f.readlines()

# %%
import numpy as np

positions = np.array([[0 if c == "." else 1 for c in l.strip()] for l in puzzle])

# %%
positions = np.concatenate(
    [
        np.concatenate([np.zeros(positions.shape) for _ in range(3)], axis=1),
        np.concatenate(
            [np.zeros(positions.shape), positions, np.zeros(positions.shape)], axis=1
        ),
        np.concatenate([np.zeros(positions.shape) for _ in range(3)], axis=1),
    ],
    axis=0,
)

# %%
from collections import deque, defaultdict


def has_neighbor(positions, coords):
    x, y = coords
    for a, b in [(-1, 0), (-1, -1), (-1, 1), (1, 0), (1, -1), (1, 1), (0, 1), (0, -1)]:
        if 0 <= (x + a) < positions.shape[0] and 0 <= (y + b) < positions.shape[1]:
            if positions[(x + a, y + b)] == 1:
                return True
    return False


# %%


def move(positions, neighbors):
    elves = np.where(positions == 1)
    propositions = defaultdict(list)
    for x, y in zip(elves[0], elves[1]):
        if has_neighbor(positions, (x, y)):
            for option in neighbors:
                if all([positions[x + a, y + b] == 0 for a, b in option]):
                    propositions[(x + option[0][0], y + option[0][1])].append((x, y))
                    break

    for to, fr in propositions.items():
        if len(fr) == 1:
            positions[to] = 1
            positions[fr[0]] = 0

    neighbors.append(neighbors.popleft())


# %%
def find_empty_tiles(positions, moves):
    pos = positions.copy()
    neighbors = deque(
        [
            [(-1, 0), (-1, -1), (-1, 1)],  # north
            [(1, 0), (1, -1), (1, 1)],  # south
            [(0, -1), (-1, -1), (1, -1)],  # west
            [(0, 1), (-1, 1), (1, 1)],  # east
        ]
    )
    for _ in range(moves):
        move(pos, neighbors)

    ones = np.where(pos == 1)
    slice = pos[ones[0].min() : ones[0].max() + 1, ones[1].min() : ones[1].max() + 1]
    return slice, np.count_nonzero(slice == 0)


# %%
p, c = find_empty_tiles(positions, 10)
print(c)
