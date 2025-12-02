"""Fetch puzzle inputs from Advent of Code."""

import os
from pathlib import Path

import requests
from dotenv import load_dotenv


def fetch_input(year: int, day: int, output_path: Path | None = None) -> str:
    """
    Fetch puzzle input from Advent of Code.

    Args:
        year: The year of the puzzle
        day: The day of the puzzle
        output_path: Optional path to save the input

    Returns:
        The puzzle input as a string

    Raises:
        ValueError: If AOC_SESSION is not set
        requests.HTTPError: If the request fails
    """
    load_dotenv()

    session = os.getenv("AOC_SESSION")
    if not session:
        raise ValueError(
            "AOC_SESSION not found. Please set it in .env file.\nSee .env.example for instructions."
        )

    url = f"https://adventofcode.com/{year}/day/{day}/input"
    cookies = {"session": session}

    response = requests.get(url, cookies=cookies, timeout=10)
    response.raise_for_status()

    input_data = response.text.strip()

    if output_path:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(input_data)

    return input_data
