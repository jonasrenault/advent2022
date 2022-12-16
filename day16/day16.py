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
            d[names.index(t), names.index(n)] = 1

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
dfs("AA", to_open, 30)

# %%
