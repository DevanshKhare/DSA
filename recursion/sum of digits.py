def sumOfDigits(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("The number has to be positive integer only")
    if n == 0:
        return 0
    return n%10 + sumOfDigits(n//10)

print(sumOfDigits(25))