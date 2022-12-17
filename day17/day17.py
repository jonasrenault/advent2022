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
# # Day 17

# %% [markdown]
# ### Part 1

# %%
# Read puzzle input
with open("input.txt", "r") as f:
    puzzle = f.readlines()

# %%
jets = [c for c in puzzle[0].strip()]

# %%
def ijets(jets):
    i = 0
    while i < len(jets):
        yield jets[i]
        i = 0 if i == len(jets) - 1 else i + 1


# %%
import numpy as np

stones = [
    np.array(((0, 0), (0, 1), (0, 2), (0, 3))),
    np.array(((0, 1), (-1, 0), (-1, 1), (-1, 2), (-2, 1))),
    np.array(((0, 0), (0, 1), (0, 2), (-1, 2), (-2, 2))),
    np.array(((0, 0), (-1, 0), (-2, 0), (-3, 0))),
    np.array(((0, 0), (0, 1), (-1, 0), (-1, 1))),
]


# %%
def push_stone(
    stone: np.ndarray, cave: np.ndarray, jet: str, bl: np.ndarray
) -> np.ndarray:
    """
    Given a stone, a cave, a jet direction and the bottom left position of the stone,
    move it in the given direction if possible

    Parameters
    ----------
    stone : np.ndarray
        the stone shape
    cave : np.ndarray
        the cave array
    jet : str
        the jet direction
    bl : np.ndarray
        the bottom left position for the stone shape

    Returns
    -------
    np.ndarray
        the moved bottom left position
    """
    dir = (0, 1) if jet == ">" else (0, -1)
    pos = stone + bl + dir
    if pos[:, 1].max() > 6 or pos[:, 1].min() < 0 or np.any(cave[tuple(pos.T)] == 1):
        return bl
    return bl + dir


# %%
from typing import Tuple


def fall_stone(
    stone: np.ndarray, cave: np.ndarray, bl: np.ndarray
) -> Tuple[bool, np.ndarray]:
    """
    Move a stone down.

    Parameters
    ----------
    stone : np.ndarray
        the stone shape
    cave : np.ndarray
        the cave
    bl : np.ndarray
        the bottom left position for the stone

    Returns
    -------
    Tuple[bool, np.ndarray]
        whether the stone moved, and its updated position
    """
    pos = stone + bl + (1, 0)
    if bl[0] == cave.shape[0] - 1 or np.any(cave[tuple(pos.T)] == 1):
        return True, bl
    return False, bl + (1, 0)


# %%
from typing import Iterator


def drop_stone(stone: np.ndarray, cave: np.ndarray, ijets: Iterator[str]):
    """
    Drop a stone in the cave.

    Parameters
    ----------
    stone : np.ndarray
        The stone shape
    cave : np.ndarray
        The cave
    ijets : Iterator[str]
        An iterator for the jet streams
    """
    high_point = (
        cave.shape[0]
        if len(cave[cave == 1]) == 0
        else np.argwhere(cave == 1)[:, 0].min()
    )
    bl = np.array((high_point - 4, 2))
    rest = False
    while not rest:
        jet = next(ijets)
        bl = push_stone(stone, cave, jet, bl)
        rest, bl = fall_stone(stone, cave, bl)
        if rest:
            cave[tuple((bl + stone).T)] = 1


# %%
def simulate(cnt):
    cave = np.zeros((10000, 7))
    gjets = ijets(jets)
    for i in range(cnt):
        stone = stones[i % 5]
        drop_stone(stone, cave, gjets)
    return cave


# %%
cave = simulate(2022)
height = cave.shape[0] - np.argwhere(cave == 1)[:, 0].min()
print(height)
