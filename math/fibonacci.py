def fibonacci(n):
    """
    Generate a Fibonacci sequence up to the given number.

    Args:
        n (int): The maximum number in the Fibonacci sequence.

    Returns:
        list: The Fibonacci sequence up to the given number.

    Example:
        >>> fibonacci(10)
        [0, 1, 1, 2, 3, 5, 8]
    """
    sequence = [0, 1]  # Initialize the sequence with the first two numbers

    while sequence[-1] < n:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)

    return sequence