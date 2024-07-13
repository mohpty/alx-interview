#!/usr/bin/python3
'''
    contains minOperations(n) function
'''


def find_factors_pairs(x):
    # Check if the input is a valid positive integer
    if x <= 0 or not isinstance(x, int):
        print("Please enter a positive integer.")
        return

    factor_pairs = []

    # Iterate from 1 to the square root of x
    for i in range(1, int(x**0.5) + 1):
        if x % i == 0:  # Check if i is a factor
            factor_pairs.append((i, x // i))

    return factor_pairs


def minOperations(n: int) -> int:
    '''
        Reaching n * H string
        in the least number of operations
    '''
    if n < 1:
        return 0
    if n == 1:
        return 1

    pairs = find_factors_pairs(n)
    if len(pairs) == 1:
        return 0

    ops = 0
    x, y = pairs[-1]
    ops += x

    # copy the factor
    ops += 1

    ops += y - 1

    return ops
