# Advent of Code 2022

Repository of my code for [Advent of Code 2022](https://adventofcode.com/2022)

## Install

Install project requirements with [poetry](https://python-poetry.org/):

```console
poetry install
```

## Session

To get the code to work with your puzzle input, you need to be logged in using your session cookie. Log in to the [Advent of Code](https://adventofcode.com/2022) website and save your session cookie in a file called `.secret-session-cookie` in the project's root directory.

## Run

Each day's problem is solved in its own python module in the [advent2022](./advent2022/) directory. To run a solution, run

```console
poetry run python advent2022/day01.py
```

## Template generation

To generate a blank template for a new day, a template generator can be used with

```console
poetry run python advent2022/utils/templates.py -d 1
```

where the `-d` option specifies the day to generate a template for.
