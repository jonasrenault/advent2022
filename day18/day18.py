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
print(surface_area(coords))

# %% [markdown]
# ### Part 2

# %%
def min_max(cubes):
    mm = tuple(
        (min([c[i] for c in cubes]) - 1, max([c[i] for c in cubes]) + 1)
        for i in range(3)
    )
    return mm


#%%
from collections import deque


def flood_3d(cubes, minmax, origin=(0, 0, 0)):
    visited = set()
    queue = deque([origin])
    surface = 0
    while queue:
        node = queue.popleft()
        visited.add(node)
        for dir in dirs:
            neighbor = tuple(node[i] + dir[i] for i in range(3))
            if all([minmax[i][0] <= neighbor[i] <= minmax[i][1] for i in range(3)]):
                if neighbor not in visited and neighbor not in queue:
                    if neighbor in cubes:
                        surface += 1
                    else:
                        queue.append(neighbor)

    return surface


# %%
mm = min_max(coords)
print(flood_3d(coords, mm))
