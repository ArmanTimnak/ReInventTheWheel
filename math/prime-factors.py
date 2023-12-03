def prime_factors(n):
    """
    Returns a list of prime factors of a given number.

    Parameters:
    n (int): The number to find prime factors for.

    Returns:
    list: A list of prime factors of the given number.

    Example:
        >>> prime_factors(12)
        [2, 2, 3]
        >>> prime_factors(15)
        [3, 5]
    """
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors