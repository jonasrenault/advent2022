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
# # Day 16

# %% [markdown]
# ### Part 1

# %%
# Read puzzle input
with open("input.txt", "r") as f:
    puzzle = f.readlines()

# %%
import re


def parse_puzzle(puzzle):
    flows = {}
    tunnels = {}
    for l in puzzle:
        m = re.match(
            "Valve (.+) has flow rate=(\d+); tunnels? leads? to valves? (.+)$",
            l.strip(),
        )
        flows[m.group(1)] = int(m.group(2))
        tunnels[m.group(1)] = m.group(3).split(", ")
    return flows, tunnels


# %%
flows, tunnels = parse_puzzle(puzzle)

# %%
import numpy as np


def compute_distances(tunnels):
    names = list(tunnels.keys())
    d = np.full((len(names), len(names)), 100)
    for n, ts in tunnels.items():
        for t in ts:
            d[names.index(n), names.index(t)] = 1

    for k in range(len(names)):
        for i in range(len(names)):
            for j in range(len(names)):
                d[i, j] = min(d[i, j], d[i, k] + d[k, j])

    return d, names


distances, names = compute_distances(tunnels)
# %%
def choose_one(options):
    for i in range(len(options)):
        yield options[i], options[:i] + options[i + 1 :]


# %%
import functools


@functools.lru_cache(maxsize=None)
def dfs(node, to_open, time_left):
    values = [
        flows[r] * (time_left - distances[names.index(node), names.index(r)] - 1)
        + dfs(r, rr, time_left - distances[names.index(node), names.index(r)] - 1)
        for r, rr in choose_one(to_open)
        if distances[names.index(node), names.index(r)] < time_left
    ]
    return max(values) if values else 0


# %%
to_open = tuple([k for k, v in flows.items() if v > 0])
print(dfs("AA", to_open, 30))

# %% [markdown]
# ### Part 2

# %% [markdown]
"""
This is the solution from [betaveros](https://github.com/betaveros/advent-of-code-2022/blob/main/p16.noul).
What it does is run dfs for one man during 26secs, then run again dfs for 26secs on remaining open valves.
It does not work on sample data, because it only works if time runs out before one man could
open all valves.
"""

# %%
def dfs2(node, to_open, time_left):
    values = [
        flows[r] * (time_left - distances[names.index(node), names.index(r)] - 1)
        + dfs2(r, rr, time_left - distances[names.index(node), names.index(r)] - 1)
        for r, rr in choose_one(to_open)
        if distances[names.index(node), names.index(r)] < time_left
    ]
    return max(values) if values else dfs("AA", to_open, 26)


# %%
print(dfs2("AA", to_open, 26))
