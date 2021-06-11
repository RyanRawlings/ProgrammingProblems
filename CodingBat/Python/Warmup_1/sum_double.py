# **********************************************************************************
#   Title: Warmup-1 > sum_double
#   URL: https://codingbat.com/prob/p141905
#   Date: 12/06/2021
#   Description: 
#     - Given two int values, return their sum. Unless the two values are 
#       the same, then return double their sum.
#************************************************************************************

# Python Ternary
def sum_double(a,b):
    return a + b if a != b else (a + b) * 2

# Test Case
print(sum_double(1,2))