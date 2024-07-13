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

# Example usage:
x = int(input("Enter a number: "))
factor_pairs = find_factors_pairs(x)
print(f"Pairs of numbers that, when multiplied, result in {x}:")
for pair in factor_pairs:
    print(pair)
