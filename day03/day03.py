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
# # Day 3

# %% [markdown]
# ### Part 1

# %%
# Read puzzle input
with open("input.txt", "r") as f:
    puzzle = f.readlines()

# %%
puzzle = [l.strip() for l in puzzle]

# %%
from collections import Counter
import string


def pack_to_priority(l):
    left = Counter(l[: len(l) // 2])
    right = Counter(l[len(l) // 2 :])
    return string.ascii_letters.index((left.keys() & right.keys()).pop()) + 1


# %%
sum(map(pack_to_priority, puzzle))

# %% [markdown]
# ### Part 2

# %%
def pack_to_group_priority(l1, l2, l3):
    item = Counter(l1).keys() & Counter(l2).keys() & Counter(l3).keys()
    return string.ascii_letters.index(item.pop()) + 1


# %%
total = 0
for i in range(0, len(puzzle) - 1, 3):
    total += pack_to_group_priority(puzzle[i], puzzle[i + 1], puzzle[i + 2])

print(total)
