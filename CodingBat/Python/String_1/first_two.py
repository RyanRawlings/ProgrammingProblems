# **********************************************************************************
#   Title: String-1 > first_two
#   URL: https://codingbat.com/prob/p184816
#   Date: 12/06/2021
#   Description: 
#     - Given a string, return the string made of its first two chars, 
#       so the String "Hello" yields "He". If the string is shorter than 
#       length 2, return whatever there is, so "X" yields "X", and the 
#       empty string "" yields the empty string "".
#************************************************************************************

# This will error if NoneType is passed in
def first_two(str):     
    return '{first_two}'.format(first_two=str[:2] if len(str)>=2 else str)

# Test Case
print(first_two('Ryan'))