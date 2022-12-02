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
# # Day 2

# %% [markdown]
# ### Part 1

# %%
# Read puzzle input
with open("input.txt", "r") as f:
    puzzle = f.readlines()


# %%
puzzle = [x.strip().split(" ") for x in puzzle]

# %%
shapes = {"X": 1, "Y": 2, "Z": 3}

scores = {
    ("A", "X"): 3,
    ("B", "Y"): 3,
    ("C", "Z"): 3,
    ("A", "Z"): 0,
    ("B", "X"): 0,
    ("C", "Y"): 0,
    ("A", "Y"): 6,
    ("B", "Z"): 6,
    ("C", "X"): 6,
}


def score_round(p1, p2):
    return shapes[p2] + scores[p1, p2]


#%%
sum([score_round(a, b) for (a, b) in puzzle])

# %% [markdown]
# ### Part 2

#%%
shapes = {"A": 1, "B": 2, "C": 3}
scores = {"X": 0, "Y": 3, "Z": 6}
plays = {
    ("A", "X"): "C",
    ("A", "Y"): "A",
    ("A", "Z"): "B",
    ("B", "X"): "A",
    ("B", "Y"): "B",
    ("B", "Z"): "C",
    ("C", "X"): "B",
    ("C", "Y"): "C",
    ("C", "Z"): "A",
}


def score_round(p1, p2):
    return scores[p2] + shapes[plays[p1, p2]]


#%%
sum([score_round(a, b) for (a, b) in puzzle])

# %%
