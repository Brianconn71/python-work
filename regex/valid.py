# import re package
import re

# function to validate landline number
def is_valid_athlone_landline_number(number):
    """
    This function takes in a string of numbers and returns true or false depending on if it meets the regex pattern requirements

    Args:
        number (string): phone number as a string to test

    Returns:
        boolean: true or false depending on validitity of number string
    """
    # set a variable to match regex pattern object
    match = re.fullmatch("090\s?64\d{5}", number)
    # if statement checking if the number string has equalled the pattern
    if match:
        # if yes return true
        return True
    else:
        # if none object returned then return false
        return False
