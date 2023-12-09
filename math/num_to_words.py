def num_to_words(num):
    """
    Converts a given number to its word representation.

    Args:
        num (int): The number to be converted.

    Returns:
        str: The word representation of the given number.

    Example:
        >>> num_to_words(123456789)
        'one hundred twenty three million four hundred fifty six thousand seven hundred eighty nine'
        >>> num_to_words(-123456789)
        'minus one hundred twenty three million four hundred fifty six thousand seven hundred eighty nine'
        >>> num_to_words(0)
        'zero'
    """
    # Define word representations for numbers 0 to 19
    ones = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
            'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    
    # Define word representations for tens multiples
    tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    
    # Define word representations for powers of 10
    powers_of_10 = ['', 'thousand', 'million', 'billion', 'trillion', 'quadrillion', 'quintillion']
    
    # Handle special cases for zero and negative numbers
    if num == 0:
        return ones[0]
    elif num < 0:
        return 'minus ' + num_to_words(abs(num))
    
    # Convert the number to words
    words = ''
    power_idx = 0
    while num > 0:
        # Get the last three digits of the number
        num_part = num % 1000
        num //= 1000
        
        # Convert the three-digit part to words
        part_words = ''
        if num_part >= 100:
            part_words += ones[num_part // 100] + ' hundred '
            num_part %= 100
        if num_part >= 20:
            part_words += tens[num_part // 10] + ' '
            num_part %= 10
        if num_part > 0:
            part_words += ones[num_part] + ' '
        
        # Add the word representation of the three-digit part to the overall words
        if part_words:
            words = part_words + powers_of_10[power_idx] + ' ' + words
        
        power_idx += 1
    
    return words.strip()