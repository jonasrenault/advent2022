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
# # Day 4

# %% [markdown]
# ### Part 1

# %%
# Read puzzle input
with open("input.txt", "r") as f:
    puzzle = f.readlines()

# %%
puzzle = [l.strip() for l in puzzle]

# %%
def intervals_overlap(line):
    left, right = line.strip().split(",")
    l1, l2 = left.split("-")
    r1, r2 = right.split("-")
    return int(
        int(l1) >= int(r1)
        and int(l2) <= int(r2)
        or int(l1) <= int(r1)
        and int(l2) >= int(r2)
    )


# %%
sum(list(map(intervals_overlap, puzzle)))

# %% [markdown]
# ### Part 2

# %%
def intervals_touch(line):
    left, right = line.strip().split(",")
    l1, l2 = left.split("-")
    r1, r2 = right.split("-")
    return int(min(int(l2), int(r2)) - max(int(l1), int(r1)) >= 0)


# %%
sum(list(map(intervals_touch, puzzle)))
