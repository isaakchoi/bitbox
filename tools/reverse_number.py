# tool: reverse_number
# description: Reverses the digits of a given number
# author: @Sreevardhan12345
# example: reverse_number "123" → "321"


def run(*args):
    """
    Reverses the digits of a given number represented as a string.

    Args:
        num_str (str): The number as a string.

    Returns:
        str: The reversed number as a string.
    """
    if len(args) != 1:
        raise ValueError("Exactly one argument is required.")
    # Check if the input is a valid number string
    if not args[0].isdigit():
        raise ValueError("Input must be a string representing a non-negative integer.")

    # Reverse the string and return it
    return args[0][::-1]