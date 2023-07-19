def add(a, b):
    # Perform integer addition using bitwise operations
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1

    return a
