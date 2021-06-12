# **********************************************************************************
#   Title: String-1 > non_start
#   URL: https://codingbat.com/prob/p127703
#   Date: 12/06/2021
#   Description: 
#     - Given 2 strings, return their concatenation, except omit the first char 
#       of each. The strings will be at least length 1.
#     - No solution provided by website
#************************************************************************************

def non_start(a,b):
    return a[1:] + b[1:]

print(non_start('Hello', 'There'))