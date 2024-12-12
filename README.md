# Advent of Code

A collection of my solutions for [Advent of Code](https://adventofcode.com/)

Coding in `python3`. May explore `TypeScript` and/or `Haskell` later for some type fun!

I use my own general utility functions that I have collected
from doing previous AoC's to speed up the boring stuff.

## Personal Stats

| Year | Stars | Score |
| ---- | ----- | ----- |
| 2015 | 10    | 0     |
| 2016 | 0     | 0     |
| 2017 | 0     | 0     |
| 2018 | 0     | 0     |
| 2019 | 36    | 0     |
| 2020 | 39    | 0     |
| 2021 | 28    | 0     |
| 2022 | 50    | 0     |
| 2023 | 50    | 0     |

## Usage

### 2024 Onwards

I have switched to using module style execution and imports. This way
I do not need to force any utilities into my PATH or site-packages.

In order to run a day's solution, from the root run
```sh
python3 -m $YEAR.$DAY

# eg. 2024 Day 7
python3 -m 2024.07 --input path/to/input
```

By default, it attempts to pull input from a file `$YEAR/$DAY.in` (eg. `2024/07.in`),
if this file is not present, it will attempt to pull input directly from
https://adventofcode.com using the [aocd](https://pypi.org/project/advent-of-code-data/)
package. This requires your token to be stored according to how `aocd`
expects it. See https://pypi.org/project/advent-of-code-data/ for a guide
to set this up.

**Notes:**
```sh
python3 -m 2024.07 --example
# is shorthand for the following to run using 
python3 -m 2024.07 --input 2024/07.ex
```

### 2023 and Before

In order to use any of my code, you will need my `/aocutils.py` file.
This contains a few useful functions I have kept handy to speed up
my solves.

Since python is so fun, importing the file in the current structure
is unlikely to work for you. I recommend moving the `aocutils.py` file
into the same directory as the file you are trying to execute.

By default, running `python3 X.py` will look for the file `X.in` as
the input file to use. So put your input in that file, or you can
specify a file with `python3 X.py your-input-file`.
