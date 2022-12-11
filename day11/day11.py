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
# # Day 11

# %% [markdown]
# ### Part 1

# %%
# Read puzzle input
with open("input.txt", "r") as f:
    puzzle = f.readlines()

# %%
def parse_puzzle(puzzle):
    monkeys = {}
    for l in puzzle:
        l = l.strip()
        if l.startswith("Monkey "):
            if int(l[len("Monkey ") : -1]) > 0:
                monkeys[len(monkeys)] = {
                    "items": items,
                    "op": op,
                    "mod": mod,
                    "send_to": send_to,
                }
            send_to = []
        elif l.startswith("Starting items: "):
            items = [int(x) for x in l[len("Starting items: ") :].split(",")]
        elif l.startswith("Operation: new = "):
            op = l[len("Operation: new = ") :]
        elif l.startswith("Test: divisible by "):
            mod = int(l[len("Test: divisible by ") :])
        elif l.startswith("If true: throw to monkey "):
            send_to.append(int(l[len("If true: throw to monkey ") :]))
        elif l.startswith("If false: throw to monkey "):
            send_to.append(int(l[len("If false: throw to monkey ") :]))
    monkeys[len(monkeys)] = {"items": items, "op": op, "mod": mod, "send_to": send_to}
    return monkeys


# %%
def play_round(monkeys, cnt):
    for i in range(len(monkeys)):
        monkey = monkeys[i]
        for item in monkey["items"]:
            old = item
            new = (eval(monkey["op"])) // 3
            if new % monkey["mod"] == 0:
                monkeys[monkey["send_to"][0]]["items"].append(new)
            else:
                monkeys[monkey["send_to"][1]]["items"].append(new)
            cnt[i] += 1
        monkey["items"] = []


# %%
from collections import Counter

cnt = Counter()
monkeys = parse_puzzle(puzzle)
for i in range(20):
    play_round(monkeys, cnt)

# %%
import math

print(math.prod([x[1] for x in cnt.most_common(2)]))

# %% [markdown]
# ### Part 2

# %%
def play_round2(monkeys, cnt):
    supermod = math.prod([m["mod"] for m in monkeys.values()])
    for i in range(len(monkeys)):
        monkey = monkeys[i]
        for item in monkey["items"]:
            old = item
            new = eval(monkey["op"])
            if new > supermod:
                new = new % supermod
            if new % monkey["mod"] == 0:
                monkeys[monkey["send_to"][0]]["items"].append(new)
            else:
                monkeys[monkey["send_to"][1]]["items"].append(new)
            cnt[i] += 1
        monkey["items"] = []


# %%
cnt = Counter()
monkeys = parse_puzzle(puzzle)
for i in range(10000):
    play_round2(monkeys, cnt)

# %%
print(math.prod([x[1] for x in cnt.most_common(2)]))
