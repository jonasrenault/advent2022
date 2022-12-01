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
# # Day 1

# %% [markdown]
# ### Part 1

# %%
# Read puzzle input
with open("input.txt", "r") as f:
    puzzle = f.readlines()


# %%
def find_highest_calories(puzzle):
    elves = []
    calories = 0
    highest = 0
    for item in puzzle:
        if item == "\n":
            elves.append(calories)
            highest = max(highest, calories)
            calories = 0
        else:
            calories += int(item.strip())
    return elves, highest


# %%
elves, highest = find_highest_calories(puzzle)
highest

# %% [markdown]
# ### Part two

# %%
highests = sorted(elves)

# %%
sum(highests[-3:])

# %%
