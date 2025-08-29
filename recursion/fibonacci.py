def fibonacci(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Invalid Input")
    if n in [0, 1]:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))