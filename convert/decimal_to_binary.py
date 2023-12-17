def decimal_to_binary(decimal):
    """
    Converts a decimal number to its binary representation.

    Args:
        decimal (int): The decimal number to be converted.

    Returns:
        str: The binary representation of the decimal number.

    Example:
        >>> decimal_to_binary(10)
        '1010'
        >>> decimal_to_binary(0)
        '0'
        >>> decimal_to_binary(1)
        '1'
    """
    if decimal == 0:
        return '0'
    
    binary = ''
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal = decimal // 2
    
    return binary
