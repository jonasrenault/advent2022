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
# # Day 15

# %% [markdown]
# ### Part 1

# %%
# Read puzzle input
with open("input.txt", "r") as f:
    puzzle = f.readlines()

# %%
import re


def parse_input(puzzle):
    sensors = {}
    for l in puzzle:
        m = re.match(
            r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)",
            l.strip(),
        )
        coords = m.groups()
        sensors[(int(m.group(1)), int(m.group(2)))] = (int(m.group(3)), int(m.group(4)))
    return sensors


# %%
sensors = parse_input(puzzle)

# %%
from typing import Tuple


def manhattan(a: Tuple[int, int], b: Tuple[int, int]) -> int:
    """
    Compute the manhattan or taxicab distance between points x and y.

    Parameters
    ----------
    x : Tuple[int, int]
        x and y coordinates for point a
    y : Tuple[int, int]
        x and y coordinates for point b

    Returns
    -------
    int
        the manhattan distance.
    """
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


# %%
from typing import List, Dict


def overlap(i1: Tuple[int, int], i2: Tuple[int, int]) -> bool:
    """
    Check if two intervals overlap.

    Example
    -------
    overlap((-3, 3), (5, 10))
        False
    overlap((-3, 3), (-1, 1))
        True

    Parameters
    ----------
    i1 : Tuple[int, int]
        A closed interval
    i2 : Tuple[int, int]
        A closed interval

    Returns
    -------
    bool
        returns True if the intervals overlap.
    """
    return (
        i2[0] <= i1[0] <= i2[1]
        or i2[0] <= i1[1] <= i2[1]
        or i1[0] <= i2[0] <= i1[1]
        or i1[0] <= i2[1] <= i1[1]
    )


def merge_intervals(
    intervals: List[Tuple[int, int]], interval: Tuple[int, int]
) -> List[Tuple[int, int]]:
    """
    Merge an interval intor a list of other intervals, reducing the list
    with overlapping intervals.

    Parameters
    ----------
    intervals : List[Tuple[int, int]]
        A list of intervals
    interval : Tuple[int, int]
        An interval

    Returns
    -------
    List[Tuple[int, int]]
        A list of intervals with no intervals overlapping
    """
    xmin, xmax = interval
    merged = []
    for i in intervals:
        if not overlap(i, interval):
            merged.append(i)
        else:
            xmin = min(i[0], xmin)
            xmax = max(i[1], xmax)
    return merged + [(xmin, xmax)]


def coverage(
    sensors: Dict[Tuple[int, int], Tuple[int, int]], y: int
) -> List[Tuple[int, int]]:
    """
    Compute the coverage for row = y, given a dict of sensors -> beacons.

    Parameters
    ----------
    sensors : Dict[Tuple[int, int], Tuple[int, int]]
        The dict of sensors -> beacon coordinates
    y : int
        the row coordinate

    Returns
    -------
    List[Tuple[int, int]]
        The list of intervals covered by the sensors at given row
    """
    cover = []
    for s, b in sensors.items():
        d = manhattan(s, b)
        step = abs(y - s[1])
        if step <= d:
            x0, x1 = (s[0] - d + step, s[0] + d - step)
            cover = merge_intervals(cover, (x0, x1))
    return cover


# %%
def blocked_units(sensors, y):
    cover = coverage(sensors, y)
    return sum([manhattan((x0, y), (x1, y)) for x0, x1 in cover])


# %%
print(blocked_units(sensors, 2000000))

# %% [markdown]
# ### Part 2

# %%
def adjacent(intervals: List[Tuple[int, int]]) -> bool:
    """
    Given a list of intervals, check if the intervals are adjacent.

    Parameters
    ----------
    intervals : List[Tuple[int, int]]
        A list of intervals

    Returns
    -------
    bool
        True if the intervals are adjacent
    """
    adjacent = True
    for i in range(len(intervals) - 1):
        adjacent &= (
            min(
                abs(intervals[i][1] - intervals[i + 1][0]),
                abs(intervals[i][0] - intervals[i + 1][1]),
            )
            == 1
        )
    return adjacent


# %%
from tqdm import tqdm


def find_distress_signal(sensors, limit):
    """
    Find the first row within limit where coverage by signal is not
    a list of adjacent intervals.
    """
    for y in tqdm(range(limit)):
        cover = coverage(sensors, y)
        if not adjacent(cover):
            print((min(cover[0][1], cover[1][1]) + 1) * 4000000 + y)
            break


# %%
find_distress_signal(sensors, 4000000)
