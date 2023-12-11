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

def nth_circular_prime(n):
    """
    Returns the nth circular prime number.

    Parameters:
    n (int): The position of the circular prime number to be found.

    Returns:
    int: The nth circular prime number.

    Example:
        >>> nth_circular_prime(1)
        2
        >>> nth_circular_prime(2)
        3
        >>> nth_circular_prime(10)
        197
    """
    count = 0
    num = 2
    while count < n:
        num_str = str(num)
        is_circular_prime = True
        for _ in range(len(num_str)):
            if not is_prime(int(num_str)):
                is_circular_prime = False
                break
            num_str = num_str[1:] + num_str[0]
        if is_circular_prime:
            count += 1
        num += 1
    return num - 1