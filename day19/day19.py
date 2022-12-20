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
# # Day 19

# %% [markdown]
# ### Part 1

# %%
# Read puzzle input
with open("input.txt", "r") as f:
    puzzle = f.readlines()

# %%
import re


def parse_blueprints(puzzle):
    blueprints = []
    for l in puzzle:
        m = re.match(
            "Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d)+ ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian.",
            l.strip(),
        )
        blueprint = tuple(int(x) for x in m.groups())
        blueprints.append(blueprint)
    return blueprints


# %%
blueprints = parse_blueprints(puzzle)

# %%
from functools import lru_cache


@lru_cache(maxsize=None)
def score_blueprint(costs, resources=(0, 0, 0), bots=(1, 0, 0), t=24):
    if t <= 1:
        return 0

    # Max number of bots we need for each resource going forward
    need_obs = bots[2] < costs[6]
    need_clay = bots[1] < costs[4]
    need_ore = bots[0] < max(costs[1], costs[2], costs[3], costs[5])

    # Which type of bot should we build ?
    build_geode = resources[0] >= costs[5] and resources[2] >= costs[6]
    build_obs = resources[0] >= costs[3] and resources[1] >= costs[4] and need_obs
    build_clay = resources[0] >= costs[2] and need_clay and need_obs
    build_ore = resources[0] >= costs[1] and need_ore

    score = 0
    if build_geode:
        # If we can build geode bot, this is the best option
        resources_ = (
            resources[0] + bots[0] - costs[5],
            resources[1] + bots[1],
            resources[2] + bots[2] - costs[6],
        )
        score = max(
            score,
            score_blueprint(costs, resources=resources_, bots=bots, t=t - 1) + t - 1,
        )
    elif build_obs:
        # If we can build obsidian bot, this is the second best option
        resources_ = (
            resources[0] + bots[0] - costs[3],
            resources[1] + bots[1] - costs[4],
            resources[2] + bots[2],
        )
        score = max(
            score,
            score_blueprint(
                costs,
                resources=resources_,
                bots=(bots[0], bots[1], bots[2] + 1),
                t=t - 1,
            ),
        )
    else:
        # Otherwise, consider building ore bot, clay bot, or simply mining
        if build_ore:
            resources_ = (
                resources[0] + bots[0] - costs[1],
                resources[1] + bots[1],
                resources[2] + bots[2],
            )
            score = max(
                score,
                score_blueprint(
                    costs,
                    resources=resources_,
                    bots=(bots[0] + 1, bots[1], bots[2]),
                    t=t - 1,
                ),
            )
        if build_clay:
            resources_ = (
                resources[0] + bots[0] - costs[2],
                resources[1] + bots[1],
                resources[2] + bots[2],
            )
            score = max(
                score,
                score_blueprint(
                    costs,
                    resources=resources_,
                    bots=(bots[0], bots[1] + 1, bots[2]),
                    t=t - 1,
                ),
            )
        resources_ = (
            resources[0] + bots[0],
            resources[1] + bots[1],
            resources[2] + bots[2],
        )
        score = max(
            score, score_blueprint(costs, resources=resources_, bots=bots, t=t - 1)
        )

    return score


# %%
def eval_bp(blueprints):
    total = 0
    for bp in blueprints:
        score = score_blueprint(bp)
        total += bp[0] * score
    return total


# %%
print(eval_bp(blueprints))

# %% [markdown]
# ### Part 2
def eval_bp_2(blueprints):
    total = 1
    for i in range(3):
        bp = blueprints[i]
        score = score_blueprint(bp, t=32)
        total *= score
    return total


# %%
print(eval_bp_2(blueprints))
