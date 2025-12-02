"""Utility functions for core methods."""

import time
from collections.abc import Callable
from functools import wraps
from typing import Any, TypeVar

from rich.console import Console

console = Console()

F = TypeVar("F", bound=Callable[..., Any])


def timing(func: F) -> F:
    """Decorator to time function execution."""

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start

        console.print(f"⏱️  {func.__name__}: {elapsed * 1000:.2f}ms", style="dim")
        return result

    return wrapper  # type: ignore
