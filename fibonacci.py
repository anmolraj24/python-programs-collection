"""
Fibonacci Sequence Module
Provides multiple implementations for computing Fibonacci numbers and series:
- Iterative generator and nth term calculation (O(n) time, O(1) space)
- Recursive calculation (O(2^n) time)
- Dynamic programming / Memoization (O(n) time, O(n) space)
- Matrix Exponentiation (O(log n) time) for huge terms
"""

import time
from functools import lru_cache
from typing import Generator, List


def fibonacci_iterative(n: int) -> int:
    """Compute the nth Fibonacci number iteratively (0-indexed, F(0)=0, F(1)=1)."""
    if not isinstance(n, int):
        raise TypeError(f"Index must be an integer, got {type(n).__name__}")
    if n < 0:
        raise ValueError(f"Fibonacci is not defined for negative indices: {n}")
    if n == 0:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def fibonacci_series(count: int) -> List[int]:
    """Generate the first `count` Fibonacci numbers as a list."""
    if count <= 0:
        return []
    if count == 1:
        return [0]
    series = [0, 1]
    while len(series) < count:
        series.append(series[-1] + series[-2])
    return series


def fibonacci_generator(limit: int) -> Generator[int, None, None]:
    """Yield Fibonacci numbers up to `limit` terms."""
    if limit <= 0:
        return
    a, b = 0, 1
    count = 0
    while count < limit:
        yield a
        a, b = b, a + b
        count += 1


@lru_cache(maxsize=1024)
def fibonacci_memoized(n: int) -> int:
    """Compute nth Fibonacci number using recursion with LRU caching."""
    if not isinstance(n, int):
        raise TypeError(f"Index must be an integer, got {type(n).__name__}")
    if n < 0:
        raise ValueError(f"Fibonacci is not defined for negative indices: {n}")
    if n <= 1:
        return n
    return fibonacci_memoized(n - 1) + fibonacci_memoized(n - 2)


def fibonacci_matrix(n: int) -> int:
    """
    Compute nth Fibonacci number using 2x2 Matrix Exponentiation in O(log n) time.
    [[F(n+1), F(n)], [F(n), F(n-1)]] = [[1, 1], [1, 0]]^n
    """
    if not isinstance(n, int):
        raise TypeError(f"Index must be an integer, got {type(n).__name__}")
    if n < 0:
        raise ValueError(f"Fibonacci is not defined for negative indices: {n}")
    if n == 0:
        return 0

    def matrix_mult(a, b):
        return [
            [a[0][0]*b[0][0] + a[0][1]*b[1][0], a[0][0]*b[0][1] + a[0][1]*b[1][1]],
            [a[1][0]*b[0][0] + a[1][1]*b[1][0], a[1][0]*b[0][1] + a[1][1]*b[1][1]]
        ]

    def matrix_pow(mat, power):
        result = [[1, 0], [0, 1]] # Identity matrix
        base = mat
        while power > 0:
            if power % 2 == 1:
                result = matrix_mult(result, base)
            base = matrix_mult(base, base)
            power //= 2
        return result

    trans_matrix = [[1, 1], [1, 0]]
    result_matrix = matrix_pow(trans_matrix, n)
    return result_matrix[0][1]


if __name__ == "__main__":
    print("=== Fibonacci Sequence Demo ===")
    print(f"First 10 terms: {fibonacci_series(10)}")
    print(f"F(20) iterative: {fibonacci_iterative(20)}")
    print(f"F(20) memoized:  {fibonacci_memoized(20)}")
    print(f"F(20) matrix:    {fibonacci_matrix(20)}")
    
    # Large number demonstration
    n_huge = 1000
    start = time.perf_counter()
    ans = fibonacci_matrix(n_huge)
    elapsed = (time.perf_counter() - start) * 1000
    print(f"\nF({n_huge}) computed via Matrix Exponentiation in {elapsed:.3f} ms:")
    print(f"Number of digits: {len(str(ans))}")
