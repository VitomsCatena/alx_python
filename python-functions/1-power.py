def pow(a, b):
    result = 1

    # Handle the base case when b is 0
    if b == 0:
        return result

    # Handle the case when b is negative
    if b < 0:
        a = 1 / a
        b = -b

    while b > 0:
        # If b is odd, multiply the result with a
        if b % 2 == 1:
            result *= a
        # Square 'a' and halve 'b'
        a *= a
        b //= 2

    return result
