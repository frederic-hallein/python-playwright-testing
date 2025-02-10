import random
import string

def generate_random_string(length=10, use_uppercase=True, use_lowercase=True, use_digits=True) -> str:
    """
    Generate a random string with customizable character sets.
    
    Args:
        length (int): Length of the string to generate
        use_uppercase (bool): Include uppercase letters
        use_lowercase (bool): Include lowercase letters
        use_digits (bool): Include digits
    
    Returns:
        str: Randomly generated string
    """
    # Build character set based on options
    char_set = ''
    if use_uppercase:
        char_set += string.ascii_uppercase
    if use_lowercase:
        char_set += string.ascii_lowercase
    if use_digits:
        char_set += string.digits
    
    # Handle case where no character sets are selected
    if not char_set:
        raise ValueError("At least one character set must be selected")
    
    # Generate random string
    return ''.join(random.choices(char_set, k=length))