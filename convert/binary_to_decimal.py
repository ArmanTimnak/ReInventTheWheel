def binary_to_decimal(binary):
    """
    Converts a binary number to its decimal equivalent.

    Args:
        binary (int): The binary number to be converted.

    Returns:
        int: The decimal equivalent of the binary number.

    Example:
        >>> binary_to_decimal(1001)
        9
        >>> binary_to_decimal(1010)
        10
        >>> binary_to_decimal(1111)
        15
    """
    decimal = 0
    power = 0
    while binary != 0:
        decimal += (binary % 10) * (2 ** power)
        binary //= 10
        power += 1
    return decimal
