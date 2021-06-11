# **********************************************************************************
#   Title: Warmup-1 > diff21
#   URL: https://codingbat.com/prob/p197466
#   Date: 11/06/2021
#   Description: 
#     - Given an int n, return the absolute difference between n and 21, 
#       except return double the absolute difference if n is over 21.
#************************************************************************************

def diff21(n):
    abs_diff = abs(21 - n)

    if n <= 21:
        return abs_diff
    else:
        return abs_diff * 2

# Test Case
# print(diff21(22))