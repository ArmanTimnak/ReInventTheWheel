def is_prime(n):
    """
    Check if a number is prime.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.

    Example:
        >>> is_prime(2)
        True
        >>> is_prime(4)
        False
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def nth_prime(n):
    """
    Returns the nth prime number.

    Parameters:
    n (int): The position of the prime number to be found.

    Returns:
    int: The nth prime number.

    Example:
        >>> nth_prime(1)
        2
        >>> nth_prime(2)
        3
        >>> nth_prime(10)
        29
    """
    count = 0
    num = 2
    while count < n:
        if is_prime(num):
            count += 1
        num += 1
    return num - 1