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
print(sum([i * signals[i - 1] for i in range(20, 221, 40)]))

# %% [markdown]
# ### Part 2

# %%
def draw_pixels(signals):
    rows = []
    for row in range(6):
        pixels = []
        for pixel in range(1, 41):
            cycle = 40 * row + pixel
            if signals[cycle - 1] <= pixel <= signals[cycle - 1] + 2:
                pixels.append("#")
            else:
                pixels.append(".")
        rows.append(pixels)
    return rows


# %%
rows = draw_pixels(signals)
for row in rows:
    print(" ".join(row))
