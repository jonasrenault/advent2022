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
# # Day 14

# %% [markdown]
# ### Part 1

# %%
# Read puzzle input
with open("input.txt", "r") as f:
    puzzle = f.readlines()

# %%
import numpy as np


def build_cave(puzzle):
    cave = np.zeros((1000, 1000))
    for l in puzzle:
        l = l.strip().split(" -> ")
        x0 = None
        y0 = None
        for c in l:
            y, x = c.split(",")
            x = int(x)
            y = int(y)
            if x == x0:
                cave[x, min(y0, y) : max(y0, y) + 1] = 1
            elif y == y0:
                cave[min(x0, x) : max(x0, x) + 1, y] = 1
            x0 = x
            y0 = y
    return cave


# %%
cave = build_cave(puzzle)
bottom = np.argwhere(cave == 1)[:, 0].max()

# %%
def drop_sand_unit(cave, bottom):
    rest = False
    x, y = 500, 0
    while not rest:
        # find lowest stopping point vertically
        low = np.argwhere(cave[y:, x] > 0)
        if low.size == 0:
            # we're falling into the abyss, break and exit
            return None

        y = low.min() - 1 + y
        # try to drop left diag
        if cave[y + 1, x - 1] == 0 and y <= bottom:
            y += 1
            x -= 1
        # try to drop right diag
        elif cave[y + 1, x + 1] == 0 and y <= bottom:
            y += 1
            x += 1
        # we stop
        else:
            rest = True
    return x, y


# %%
def fill_cave(cave, bottom):
    c = cave.copy()
    res = drop_sand_unit(c, bottom)
    cnt = 0
    while res is not None:
        x, y = res
        c[y, x] = 2
        cnt += 1
        res = drop_sand_unit(c, bottom)
    return cnt


# %%
print(fill_cave(cave, bottom))

# %% [markdown]
# ### Part 2

# %%
def fill_cave_floored(cave, bottom):
    c = cave.copy()
    c[bottom + 2, :] = 1
    res = drop_sand_unit(c, bottom)
    cnt = 0
    while res is not None and res != (500, 0):
        x, y = res
        c[y, x] = 2
        cnt += 1
        res = drop_sand_unit(c, bottom)
    return cnt + 1


# %%
print(fill_cave_floored(cave, bottom))
