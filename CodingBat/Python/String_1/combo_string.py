# **********************************************************************************
#   Title: String-1 > combo_string
#   URL: https://codingbat.com/prob/p194053
#   Date: 12/06/2021
#   Description: 
#     - Given 2 strings, a and b, return a string of the form short+long+short, 
#       with the shorter string on the outside and the longer string on the inside. 
#       The strings will not be the same length, but they may be empty (length 0)
#     - No solution provided by website
#************************************************************************************

def combo_string(a, b):
    short_string = ''
    long_string = ''

    if len(a) > len(b):
        short_string = b
        long_string = a
    else:
        short_string = a
        long_string = b

    return short_string + long_string + short_string
  
print(combo_string('a', 'b'))