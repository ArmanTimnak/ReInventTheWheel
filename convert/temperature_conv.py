def temperature_conv(value, input_unit, output_unit):
    """
    Convert temperature from one unit to another.

    Args:
        value (float): The value of the temperature to be converted.
        input_unit (str): The unit of the input temperature (C, F, or K).
        output_unit (str): The unit of the output temperature (C, F, or K).

    Returns:
        float: The converted temperature value.

    Example:
        >>> temperature_conv(0, 'C', 'F')
        32.0
        >>> temperature_conv(32, 'F', 'C')
        0.0
        >>> temperature_conv(0, 'C', 'K')
        273.15
        >>> temperature_conv(273.15, 'K', 'C')
        0.0
        >>> temperature_conv(32, 'F', 'K')
        273.15
        >>> temperature_conv(273.15, 'K', 'F')
        32.0
    """
    if input_unit == 'C' and output_unit == 'F':
        return (value * 9/5) + 32
    elif input_unit == 'F' and output_unit == 'C':
        return (value - 32) * 5/9
    elif input_unit == 'C' and output_unit == 'K':
        return value + 273.15
    elif input_unit == 'K' and output_unit == 'C':
        return value - 273.15
    elif input_unit == 'F' and output_unit == 'K':
        return (value + 459.67) * 5/9
    elif input_unit == 'K' and output_unit == 'F':
        return (value * 9/5) - 459.67
    else:
        return value