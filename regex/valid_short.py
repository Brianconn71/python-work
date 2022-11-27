# import re package
import re

# function to validate a short file name
def is_valid_short_filename(filename):
    """
    This function takes in a string of a file name and returns true or false depending on if it meets the regex pattern requirements

    Args:
        filename (string): filename as a string to test

    Returns:
        boolean: true or false depending on validitity of the file name
    """
    # set a variable to match regex pattern object
    match = re.fullmatch("[a-zA-Z0-9-_]{1,8}\.?[a-zA-Z0-9_-]{1,3}?", filename)
    # if statement checking if the filename string has equalled the pattern
    if match:
        # if yes return true
        return True
    else:
        # if none object returned then return false
        return False
