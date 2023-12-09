def factorial(n):
    """
    Calculate the factorial of a non-negative integer.

    Parameters:
    n (int): The number for which factorial is to be calculated.

    Returns:
    int: The factorial of the given number.

    Example:
        >>> factorial(5)
        120
        >>> factorial(0)
        1
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)