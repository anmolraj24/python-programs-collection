"""
Factorial Calculation Module
Provides multiple approaches to computing factorials in Python:
- Iterative approach (O(n) time, O(1) space)
- Recursive approach (O(n) time, O(n) call stack)
- Memoized approach (O(n) time with cached results)
"""

import time
from functools import lru_cache
from typing import Dict


def factorial_iterative(n: int) -> int:
    """Calculate factorial of n using an iterative loop."""
    if not isinstance(n, int):
        raise TypeError(f"Factorial is only defined for integers, got {type(n).__name__}")
    if n < 0:
        raise ValueError(f"Factorial is not defined for negative numbers: {n}")
    if n in (0, 1):
        return 1

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def factorial_recursive(n: int) -> int:
    """Calculate factorial of n using recursion."""
    if not isinstance(n, int):
        raise TypeError(f"Factorial is only defined for integers, got {type(n).__name__}")
    if n < 0:
        raise ValueError(f"Factorial is not defined for negative numbers: {n}")
    if n in (0, 1):
        return 1

    return n * factorial_recursive(n - 1)


@lru_cache(maxsize=1024)
def factorial_memoized(n: int) -> int:
    """Calculate factorial of n with LRU caching for high-throughput calls."""
    if not isinstance(n, int):
        raise TypeError(f"Factorial is only defined for integers, got {type(n).__name__}")
    if n < 0:
        raise ValueError(f"Factorial is not defined for negative numbers: {n}")
    if n in (0, 1):
        return 1

    return n * factorial_memoized(n - 1)


def compare_factorial_performance(n: int = 500, iterations: int = 1000) -> Dict[str, float]:
    """Benchmark performance between iterative, recursive, and memoized methods."""
    print(f"--- Benchmarking Factorial(n={n}) over {iterations} iterations ---")
    
    # 1. Iterative
    start = time.perf_counter()
    for _ in range(iterations):
        factorial_iterative(n)
    time_iter = time.perf_counter() - start

    # 2. Recursive (with safe depth)
    safe_n = min(n, 900)
    start = time.perf_counter()
    for _ in range(iterations):
        factorial_recursive(safe_n)
    time_rec = time.perf_counter() - start

    # 3. Memoized
    factorial_memoized.cache_clear()
    start = time.perf_counter()
    for _ in range(iterations):
        factorial_memoized(n)
    time_memo = time.perf_counter() - start

    results = {
        "Iterative (s)": round(time_iter, 5),
        f"Recursive (n={safe_n}) (s)": round(time_rec, 5),
        "Memoized (s)": round(time_memo, 5),
    }

    for method, elapsed in results.items():
        print(f"{method}: {elapsed}s")

    return results


if __name__ == "__main__":
    print("=== Factorial Calculation Demo ===")
    test_values = [0, 1, 5, 10, 15]
    for val in test_values:
        print(f"{val}! = {factorial_iterative(val)}")

    print("\nBenchmarking:")
    compare_factorial_performance(n=200, iterations=5000)
