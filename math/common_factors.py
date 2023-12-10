def common_factors(numbers):
    """
    Returns a set of common factors of the given numbers.
    
    Parameters:
    numbers (int): The numbers to find common factors for.
    
    Returns:
    set: A set of common factors.

    Example:
        >>> common_factors(12, 15)
        {3}
        >>> common_factors(12, 15, 20)
        {4, 5}
    """
    factors = set()
    smallest_number = min(numbers)
    
    for i in range(1, smallest_number + 1):
        if all(num % i == 0 for num in numbers):
            factors.add(i)
    
    return factors