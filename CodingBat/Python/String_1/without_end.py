# **********************************************************************************
#   Title: String-1 > without_end
#   URL: https://codingbat.com/prob/p138533
#   Date: 12/06/2021
#   Description: 
#     - Given a string, return a version without the first and last char,
#       so "Hello" yields "ell". The string length will be at least 2.
#     - No solution provided by website
#************************************************************************************

# Start from the second index and end at the second index (reversed)
def without_end(str):
    return str[1:-1]

print(without_end('Ryan'))