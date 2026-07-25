"""Utility functions — some good, some not."""

import time
from functools import lru_cache


# Bad: recalculates every call
def fibonacci(n):
    """Return the nth Fibonacci number."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# Good: cached
@lru_cache(maxsize=None)
def fibonacci_cached(n):
    """Return the nth Fibonacci number (cached)."""
    if n <= 1:
        return n
    return fibonacci_cached(n - 1) + fibonacci_cached(n - 2)


# Bad: O(n^2) — repeated string concatenation
def build_report_bad(entries):
    """Build a report string from entries."""
    result = ""
    for entry in entries:
        result += f"Item: {entry}\n"
    return result


# Good: O(n) — list + join
def build_report_good(entries):
    """Build a report string from entries."""
    lines = [f"Item: {e}" for e in entries]
    return "\n".join(lines)


# Bad: sleeps in a loop
def poll_status_bad(url, timeout=30):
    """Poll a URL until timeout."""
    deadline = time.time() + timeout
    while time.time() < deadline:
        # Check status...
        time.sleep(0.1)
    return False


# Good: adaptive polling
def poll_status_good(url, timeout=30):
    """Poll a URL with adaptive backoff."""
    deadline = time.time() + timeout
    delay = 0.1
    while time.time() < deadline:
        # Check status...
        time.sleep(delay)
        delay = min(delay * 1.5, 5.0)
    return False
