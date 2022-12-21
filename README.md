# Advent of Code 2022

Repository of my code for [Advent of Code 2022](https://adventofcode.com/2022)

## Install

Create an environnment with python >= 3.10, for example using [mamba](https://mamba.readthedocs.io/en/latest/)

```bash
mamba create -n advent python=3.10
mamba activate advent
```

then install requirements into the environment. With [poetry](https://python-poetry.org/):

```bash
poetry install --with dev
```

or with pip

```bash
pip install -r requirements.txt
```

## Structure

Each day's problem is in its own directory. Each day's directory contains an `input.txt` file.
**Warning: these are my input files, input files are different for each user so results may differ.**

The code for each day's problem is in a python script file. The script files use jupytext percent format and can be run as notebooks.

## Execution

To run the script files as notebooks, start a jupyter lab server with :

```bash
jupyter lab
```

then right click on the script file in the explorer and select `Open with Notebook`.

To run the script files as python scripts, run each script from its own directory :

```bash
cd day01
python day01.py
```

The root script `run.sh` will cd into each directory and execute its script.
