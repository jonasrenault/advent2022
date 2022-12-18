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
# # Day 18

# %% [markdown]
# ### Part 1

# %%
# Read puzzle input
with open("input.txt", "r") as f:
    puzzle = f.readlines()

# %%
coords = {tuple([int(x) for x in l.strip().split(",")]) for l in puzzle}

# %%
dirs = {(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)}


def surface_area(cubes):
    surface = 0
    for cube in cubes:
        for dir in dirs:
            neighbor = tuple(cube[i] + dir[i] for i in range(3))
            if neighbor not in cubes:
                surface += 1
    return surface


# %%
surface_area(coords)
