# **********************************************************************************
#   Title: String-1 > extra_end
#   URL: https://codingbat.com/prob/p148853
#   Date: 12/06/2021
#   Description: 
#     - Given a string, return a new string made of 3 copies of the last 2 
#       chars of the original string. The string length will be at least 2.
#************************************************************************************

# This won't through error for NoneType concatenation
def extra_end(str):
    return '{last_two}{last_two}{last_two}'.format(last_two=str[-2:])

# Test Case
print(extra_end('Ryan'))