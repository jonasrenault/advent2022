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
# parse puzzle
crates = [l for l in puzzle if not l.startswith("move")][:-2]
ops = [l for l in puzzle if l.startswith("move")]

# %%
# stack crates into piles
from collections import defaultdict

piles = defaultdict(list)
for l in crates:
    for i in range(len(l) // 4):
        if l[1 + 4 * i] != " ":
            piles[i + 1].append(l[1 + 4 * i])

# %%
# apply ops to move crates from piles
import re

for op in ops:
    m = re.match(r"move (\d+) from (\d+) to (\d+)", op)
    (qty, fr, to) = int(m.group(1)), int(m.group(2)), int(m.group(3))
    piles[to] = piles[fr][: int(qty)][::-1] + piles[to]
    piles[fr] = piles[fr][int(qty) :]

# %%
# print top crates for each pile
tops = [piles[i + 1][0] for i in range(max(piles.keys()))]
"".join(tops)
