# Advent of Code

A collection of my solutions for [Advent of Code](https://adventofcode.com/) solved in Python 3.12

## Personal Stats

| Year | Stars | Score |
| ---- | ----- | ----- |
| 2015 | 50    | 0     |
| 2016 | 50    | 0     |
| 2017 | 50    | 0     |
| 2018 | 36    | 0     |
| 2019 | 36    | 0     |
| 2020 | 39    | 0     |
| 2021 | 39    | 0     |
| 2022 | 50    | 0     |
| 2023 | 50    | 0     |
| 2024 | 50    | 0     |
| Tot  | 450   | 0     |

## Usage

```bash
# Install in development mode
pip install -e ".[dev]"
```

### Quick Start

1. Set your Advent of Code session cookie:
```bash
echo "AOC_SESSION=your_session_cookie_here" > .env
```

2. Create a new day:
```bash
aoc new 2015 1
```

3. Solve the problem in `src/advent/solutions/year_2015/day_01.py`

4. Run your solution:
```bash
aoc run 2015 1
```

### Development

```bash
# Run tests
pytest

# Lint code
ruff check .

# Type check
mypy src/

# Format code
ruff format .
```
