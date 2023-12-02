def lcm(numbers):
    """
    Calculates the least common multiple (LCM) of a list of numbers.

    Args:
        numbers (list): A list of integers.

    Returns:
        int: The least common multiple of the numbers.

    Example:
        >>> lcm([2, 3, 4])
        12
        >>> lcm([5, 10, 15])
        30
    """
    lcm_result = 1
    max_num = max(numbers)
    i = 2
    while i <= max_num:
        divisible = False
        for num in numbers:
            if num % i == 0:
                divisible = True
                break
        if divisible:
            lcm_result *= i
            for j in range(len(numbers)):
                if numbers[j] % i == 0:
                    numbers[j] //= i
        else:
            i += 1
    for num in numbers:
        lcm_result *= num
    return lcm_result