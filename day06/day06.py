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
# # Day 5

# %% [markdown]
# ### Part 1

# %%
# Read puzzle input
with open("input.txt", "r") as f:
    puzzle = f.readlines()

# %%
puzzle = puzzle[0].strip()

# %%
from collections import Counter


def find_unique_marker(puzzle: str, unique: int):
    pos = None
    for i in range(unique, len(puzzle)):
        if len(Counter(puzzle[i - unique : i])) == unique:
            pos = i
            break
    return pos


print(find_unique_marker(puzzle, 4))

# %% [markdown]
# ### Part 2

#%%
print(find_unique_marker(puzzle, 14))
