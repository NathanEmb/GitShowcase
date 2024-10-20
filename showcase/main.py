def greater_than_five(input: int, inclusive: bool = False) -> bool:
    """ Returns True if input is greater than 5, False otherwise.

    :param input: The input to check.
    :param inclusive: If True, the function will return True if input is equal to 5.
    :return: True if input is greater than 5, False otherwise.
    """
    
    if inclusive:
        return input >= 5

    return input > 5
