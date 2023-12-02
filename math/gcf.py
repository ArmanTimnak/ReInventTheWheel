def gcf(numbers):
    """
    Calculates the greatest common factor (GCF) of a list of numbers.

    Parameters:
    numbers (list): A list of numbers for which the GCF needs to be calculated.

    Returns:
    int: The greatest common factor of the given numbers.

    Example:
        >>> gcf([20, 12, 8])
        4
        >>> gcf([5, 10, 15])
        5
    """
    def find_gcf(a, b):
        while b:
            a, b = b, a % b
        return a

    gcf = numbers[0]
    for number in numbers[1:]:
        gcf = find_gcf(gcf, number)
    return gcf