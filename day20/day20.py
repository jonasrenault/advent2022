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
# # Day 20

# %% [markdown]
# ### Part 1

# %%
# Read puzzle input
with open("input.txt", "r") as f:
    puzzle = f.readlines()

# %%
def mix(puzzle):
    nums = [int(c.strip()) for c in puzzle]
    size = len(nums)
    orders = list(range(size))

    for i in range(size):
        pos = orders.index(i)
        element = nums[pos]
        new_pos = (pos + element) % (size - 1)

        nums.insert(new_pos, nums.pop(pos))
        orders.insert(new_pos, orders.pop(pos))

    zero_i = nums.index(0)
    return sum([nums[(i + zero_i) % size] for i in range(1000, 4000, 1000)])


# %%
print(mix(puzzle))

# %% [markdown]
# ### Part 2

# %%
def mix2(puzzle):
    nums = [811589153 * int(c.strip()) for c in puzzle]
    size = len(nums)
    orders = list(range(size))

    for i in range(10):
        for i in range(size):
            pos = orders.index(i)
            element = nums[pos]
            new_pos = (pos + element) % (size - 1)

            nums.insert(new_pos, nums.pop(pos))
            orders.insert(new_pos, orders.pop(pos))

    zero_i = nums.index(0)
    return sum([nums[(i + zero_i) % size] for i in range(1000, 4000, 1000)])


# %%
print(mix2(puzzle))
