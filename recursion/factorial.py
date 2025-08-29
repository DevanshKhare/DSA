def factorial(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("The number must be non-negative integer only")
    if n in [0, 1]:
        return 1
    return n * factorial(n-1)

print(factorial(5))