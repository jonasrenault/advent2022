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
# # Day 12

# %% [markdown]
# ### Part 1

# %%
# Read puzzle input
with open("input.txt", "r") as f:
    puzzle = f.readlines()


# %%
import numpy as np

puzzle = [[ord(c) for c in l.strip()] for l in puzzle]
puzzle = np.array(puzzle)

# %%
dirs = {(1, 0), (0, 1), (-1, 0), (0, -1)}


def path(pos, seen, puzzle, end):
    if np.all(pos == end):
        return seen + [tuple(pos)]
    current = puzzle[tuple(pos)]
    possible = [pos + x for x in dirs]
    possible = list(
        filter(
            lambda x: tuple(x) not in seen
            and 0 <= x[0] < puzzle.shape[0]
            and 0 <= x[1] < puzzle.shape[1]
            and (puzzle[tuple(x)] < current or puzzle[tuple(x)] <= current + 1),
            possible,
        )
    )
    if not possible:
        return list(range(puzzle.size))

    paths = [path(x, seen + [tuple(pos)], puzzle, end) for x in possible]
    return min(paths, key=lambda x: len(x))


# %%
start = np.argwhere(puzzle == ord("S"))[0]
end = np.argwhere(puzzle == ord("E"))[0]
input = puzzle.copy()
input[tuple(start)] = ord("a")
input[tuple(end)] = ord("z")
p = path(start, [], input, end)

# %%
