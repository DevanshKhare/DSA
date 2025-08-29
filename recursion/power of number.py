def powerOfNumber(base, exp):
    if not isinstance(exp, int):
        raise ValueError("The exponent must be integer number only")
    if exp == 0:
        return 1
    elif exp < 0:
        return 1/base * powerOfNumber(base, exp+1)
    return base * powerOfNumber(base, exp-1)

print(powerOfNumber(4,2))