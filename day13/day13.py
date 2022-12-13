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
# # Day 13

# %% [markdown]
# ### Part 1

# %%
# Read puzzle input
with open("input.txt", "r") as f:
    puzzle = f.readlines()


# %%
def validate_pairs(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left == right:
            return None
        return left < right
    elif isinstance(left, list) and isinstance(right, list):
        for l, r in zip(left, right):
            res = validate_pairs(l, r)
            if res is None:
                continue
            else:
                return res
        if len(left) == len(right):
            return None
        return len(left) < len(right)
    elif isinstance(left, int):
        return validate_pairs([left], right)
    else:
        return validate_pairs(left, [right])


# %%
valid = []
for i in range(0, len(puzzle), 3):
    left = eval(puzzle[i].strip())
    right = eval(puzzle[i + 1].strip())
    if validate_pairs(left, right):
        valid.append(1 + i // 3)

print(sum(valid))

# %% [markdown]
# ### Part 2

# %%
packets = [eval(l.strip()) for l in puzzle if l.strip() != ""]

# %%
def bubble_sort(packets):
    sorted = True
    while sorted:
        sorted = False
        for i in range(len(packets) - 1):
            l = packets[i]
            r = packets[i + 1]
            if not validate_pairs(l, r):
                packets[i + 1] = l
                packets[i] = r
                sorted = True

    return packets


# %%
sorted = bubble_sort(packets + [[[2]], [[6]]])
print((sorted.index([[6]]) + 1) * (sorted.index([[2]]) + 1))
