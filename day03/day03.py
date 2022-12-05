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
from collections import Counter
import string


def pack_to_priority(l):
    left = Counter(l[: len(l) // 2])
    right = Counter(l[len(l) // 2 :])
    return string.ascii_letters.index((left.keys() & right.keys()).pop()) + 1


# %%
sum(map(pack_to_priority, puzzle))

# %%
