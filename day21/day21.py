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
# # Day 21

# %% [markdown]
# ### Part 1

# %%
# Read puzzle input
with open("input.txt", "r") as f:
    puzzle = f.readlines()

# %%
import re
import operator

ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
}


def parse_monkeys(puzzle):
    monkeys = {}
    for l in puzzle:
        m = re.match(r"(.+): (\d+)", l.strip())
        if m:
            monkeys[m.group(1)] = int(m.group(2))
        else:
            m = re.match(r"(.+): ([^\+\/\-\*]+) ([\+\/\-\*]) ([^\+\/\-\*]+)", l.strip())
            monkeys[m.group(1)] = (m.group(2), ops[m.group(3)], m.group(4))
    return monkeys


# %%
monkeys = parse_monkeys(puzzle)
# %%
def eval_monkeys(monkeys):
    while isinstance(monkeys["root"], tuple):
        for monkey, op in monkeys.items():
            if (
                isinstance(op, tuple)
                and not isinstance(monkeys[op[0]], tuple)
                and not isinstance(monkeys[op[2]], tuple)
            ):
                monkeys[monkey] = op[1](monkeys[op[0]], monkeys[op[2]])


# %%
eval_monkeys(monkeys)
# %%
print(int(monkeys["root"]))
# %%
