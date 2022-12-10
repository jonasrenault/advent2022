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
# # Day 10

# %% [markdown]
# ### Part 1

# %%
# Read puzzle input
with open("input.txt", "r") as f:
    puzzle = f.readlines()


# %%
def parse_signal(puzzle, signals):
    for op in puzzle:
        signals.append(signals[-1])
        if op.strip() != "noop":
            v = int(op.strip()[5:])
            signals.append(v + signals[-1])


# %%
signals = [1]
parse_signal(puzzle, signals)

# %%
sum([i * signals[i - 1] for i in range(20, 221, 40)])
