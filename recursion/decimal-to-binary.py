def decimalToBinary(n):
    if not isinstance(n, int):
        return ValueError("The parameter must be in integer only")
    if n == 0:
        return 0
    return n%2 + 10 * decimalToBinary(n//2)

print(decimalToBinary(13))