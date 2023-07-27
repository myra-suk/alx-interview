#!/usr/bin/python3
"""
A method that validates whether a given data set
represents UTF-8 encoding
"""


def validUTF8(data):
    """
    function to validate utf-8 encoding
    Args:
        data(list): data set containing multiple characters
    Returns:
        boolean: true if the data is valid utf-8 encoded, 
        otherwise false
    """
    count = 0
    
    
    for x in data:

        if 191 >= x >= 128:

            if not count:
                return False

            count -= 1
        else:
            if count:
                return False

            if x < 128:
                continue
            elif x < 224:
                count = 1
            elif x < 240:
                count = 2
            elif x < 248:
                count = 3
            else:
                return False

    return count == 0
