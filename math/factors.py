def factors(num):
    """
    Returns a list of factors of the given number.

    Parameters:
    num (int): The number to find factors for.

    Returns:
    list: A list of factors of the given number.

    Example:
        >>> factors(12)
        [1, 2, 3, 4, 6, 12]
        >>> factors(98)
        [1, 2, 7, 14, 49, 98]
    """
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors