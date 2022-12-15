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
def manhattan(x, y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1])


# %%
def taxicab_ball(center, radius):
    x = center[0]
    y = center[1]
    rows = []
    for r in range(radius + 1):
        rows.append([(x - radius + r, y - r), (x + radius - r, y - r)])
        if r > 0:
            rows.append([(x - radius + r, y + r), (x + radius - r, y + r)])
    return rows


# %%
manhattan((8, 7), (2, 11))
taxicab_ball((-8, -7), 9)
# %%
def coverage(sensors, y):
    minx = None
    maxx = None
    for sensor, beacon in sensors.items():
        d = manhattan(sensor, beacon)
        ball = taxicab_ball(sensor, d)
        if sensor[1] - d <= y <= sensor[1] + d:
            for row in filter(lambda x: x[0][1] == y, ball):
                if minx is None or row[0][0] < minx:
                    minx = row[0][0]
                if maxx is None or row[1][0] > maxx:
                    maxx = row[1][0]
    return minx, maxx


# %%
y = 2000000
minx, maxx = coverage(sensors, y)
print(
    manhattan((minx, y), (maxx, y))
    + 1
    - len(list(filter(lambda x: x[1] == y, set(sensors.values()))))
)
