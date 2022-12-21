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

inv_ops = {
    operator.sub: operator.add,
    operator.add: operator.sub,
    operator.truediv: operator.mul,
    operator.mul: operator.truediv,
}

# %%
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
def solve_for_monkey(monkeys, monkey):
    value = monkeys[monkey]
    if isinstance(value, int):
        return value
    left, op, right = value
    return op(solve_for_monkey(monkeys, left), solve_for_monkey(monkeys, right))


print(int(solve_for_monkey(monkeys, "root")))
# %% [markdown]
# ### Part 2

# %%
def solve_for_human(monkeys):
    monkeys["humn"] = "x"
    left, op, right = monkeys["root"]
    try:
        value = solve_for_monkey(monkeys, right)
    except ValueError:
        tosolve = right
        value = solve_for_monkey(monkeys, left)
    else:
        tosolve = left
    return solve_for_x(monkeys, tosolve, value)


def solve_for_x(monkeys, monkey, value):
    if monkey == "humn":
        return value
    left, op, right = monkeys[monkey]
    try:
        rval = solve_for_monkey(monkeys, right)
    except ValueError:
        if op == operator.sub:
            value = -value
        lval = solve_for_monkey(monkeys, left)
        return solve_for_x(monkeys, right, inv_ops[op](value, lval))
    else:
        return solve_for_x(monkeys, left, inv_ops[op](value, rval))


# %%
print(int(solve_for_human(monkeys)))
