"""Core utilities for AoC solver."""

from .fetcher import fetch_input
from .solver import Solver
from .utils import timing

__all__ = ["Solver", "fetch_input", "timing"]
