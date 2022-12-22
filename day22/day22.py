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
# # Day 22

# %% [markdown]
# ### Part 1

# %%
# Read puzzle input
with open("input.txt", "r") as f:
    puzzle = f.readlines()

# %%
import numpy as np

chr_to_int = {" ": 1, ".": 0, "#": 2}


def parse_board(puzzle):
    max_length = max([len(l.strip("\n")) for l in puzzle[:-2]])
    rows = []
    for l in puzzle[:-2]:
        rows.append([chr_to_int[c] for c in l.strip("\n").ljust(max_length, " ")])

    return np.array(rows)


# %%
board = parse_board(puzzle)
instructions = puzzle[-1].strip()


# %%
dirs = {
    0: (0, 1),  # >
    1: (1, 0),  # v
    2: (0, -1),  # <
    3: (-1, 0),  # ^
}


def neighbor(board, pos, dir):
    d = dirs[dir]
    n = (pos[0] + d[0], pos[1] + d[1])
    if (
        n[0] >= board.shape[0]
        or n[0] < 0
        or n[1] < 0
        or n[1] >= board.shape[1]
        or board[n] == 1
    ):
        if dir == 0:
            n = (n[0], np.where(board[n[0], :] != 1)[0].min())
        elif dir == 2:
            n = (n[0], np.where(board[n[0], :] != 1)[0].max())
        elif dir == 1:
            n = (np.where(board[:, n[1]] != 1)[0].min(), n[1])
        else:
            n = (np.where(board[:, n[1]] != 1)[0].max(), n[1])
    return n


def move(board, pos, dir, units):
    if units == 0:
        return pos

    n = neighbor(board, pos, dir)
    if board[n] == 2:
        return pos

    return move(board, n, dir, units - 1)


# %%
import re


def run_instructions(board, instructions):
    dir = 0
    pos = (0, np.where(board[0, :] != 1)[0].min())
    ii = re.split("([LR])", instructions)
    for i in ii:
        try:
            i = int(i)
            pos = move(board, pos, dir, i)
        except ValueError:
            dir = (dir + 1) % 4 if i == "R" else (dir - 1) % 4
        except IndexError as e:
            print(board, pos, dir, i)
            raise e
    return 1000 * (pos[0] + 1) + 4 * (pos[1] + 1) + dir


# %%
print(run_instructions(board, instructions))
