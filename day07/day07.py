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
# # Day 7

# %% [markdown]
# ### Part 1

# %%
# Read puzzle input
with open("input.txt", "r") as f:
    puzzle = f.readlines()


# %%
import re
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Tuple


def parse_op(
    contents: Dict[Path, List[Path | Tuple[str, int]]], cwd: Path, op: str
) -> Path:
    """
    Parse op string and build contents dict.

    Parameters
    ----------
    contents : Dict[Path, List[Path  |  Tuple[str, int]]]
        A dict of file_path -> list of files and dirs
    cwd : Path
        current working directory path
    op : str
        the op to parse

    Returns
    -------
    Path
        the updated cwd
    """
    m = re.match(r"(\d+) (.+)", op)

    if op == "$ cd ..":
        cwd = cwd.parent
    elif op == "$ cd /":
        cwd = Path("/")
    elif op.startswith("$ cd "):
        dir = op[5:]
        cwd = cwd / dir
    elif op.startswith("dir"):
        dir = op[4:]
        contents[cwd].append(cwd / dir)
    elif m is not None:
        size, file = m.groups()
        contents[cwd].append((file, int(size)))

    return cwd


# %%
contents = defaultdict(list)
cwd = Path("/")

# Parse list of ops and build contents tree
for op in puzzle:
    cwd = parse_op(contents, cwd, op.strip())

# %%
def compute_size(
    dir: Path,
    contents: Dict[Path, List[Path | Tuple[str, int]]],
    sizes: Dict[Path, int],
) -> Dict[Path, int]:
    """
    Given a directory path, compute it's size based on the contents tree.

    Parameters
    ----------
    dir : Path
        the directory path to compute the size for.
    contents : Dict[Path, List[Path  |  Tuple[str, int]]]
        the contents tree
    sizes : Dict[Path, int]
        A dict containing sizes for the given dir and its sub directories

    Returns
    -------
    Dict[Path, int]
        a dict of sizes
    """
    if dir in sizes:
        return sizes[dir]
    size = sum(
        [
            f[1] if isinstance(f, tuple) else compute_size(f, contents, sizes)
            for f in contents[dir]
        ]
    )
    sizes[dir] = size
    return size


sizes = {}
compute_size(Path("/"), contents, sizes)

# %%
print(sum([v for v in sizes.values() if v <= 100000]))
