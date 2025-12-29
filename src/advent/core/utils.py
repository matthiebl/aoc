"""Utility functions for core methods."""

import time
from collections.abc import Callable
from functools import partial, wraps
from typing import Any

from rich.console import Console

console = Console()


def timing[F: Callable](func: F | None = None, *, store: bool = False, verbose: bool = True) -> F:
    """Decorator to time function execution."""

    if func is None:
        return partial(timing, store=store, verbose=verbose)  # type: ignore

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = round((time.perf_counter() - start) * 1000, 2)

        if verbose:
            console.print(f"⏱️  {func.__name__}: {elapsed}ms", style="dim")
        if store:
            return result, elapsed
        return result

    return wrapper  # type: ignore
