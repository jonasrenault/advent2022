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
from typing import Dict, List


def create_piles(crates: List[str]) -> Dict[int, List[str]]:
    piles = defaultdict(list)
    for l in crates:
        for i in range(len(l) // 4):
            if l[1 + 4 * i] != " ":
                piles[i + 1].append(l[1 + 4 * i])
    return piles


# %%
# apply ops to move crates from piles
import re


def apply_ops(ops: List[str], piles: Dict[int, List[str]]) -> Dict[int, List[str]]:
    for op in ops:
        m = re.match(r"move (\d+) from (\d+) to (\d+)", op)
        (qty, fr, to) = int(m.group(1)), int(m.group(2)), int(m.group(3))
        piles[to] = piles[fr][: int(qty)][::-1] + piles[to]
        piles[fr] = piles[fr][int(qty) :]
    return piles


# %%
# print top crates for each pile
piles = apply_ops(ops, create_piles(crates))
tops = [piles[i + 1][0] for i in range(max(piles.keys()))]
print("".join(tops))

# %% [markdown]
# ### Part 2

# %%
def apply_ops(
    ops: str, piles: Dict[int, List[int]], reverse: bool
) -> Dict[int, List[int]]:
    for op in ops:
        m = re.match(r"move (\d+) from (\d+) to (\d+)", op)
        (qty, fr, to) = int(m.group(1)), int(m.group(2)), int(m.group(3))
        moved = piles[fr][: int(qty)]
        if reverse:
            moved = moved[::-1]
        piles[to] = moved + piles[to]
        piles[fr] = piles[fr][int(qty) :]
    return piles


# %%
# print top crates for each pile
piles = apply_ops(ops, create_piles(crates), False)
tops = [piles[i + 1][0] for i in range(max(piles.keys()))]
print("".join(tops))
