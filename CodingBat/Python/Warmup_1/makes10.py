# **********************************************************************************
#   Title: Warmup-1 > makes10
#   URL: https://codingbat.com/prob/p124984
#   Date: 11/06/2021
#   Description: 
#     - Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.
#************************************************************************************

def makes10(a,b):
    return (a == 10 or b == 10 or a + b == 10)

# Test Case
print(makes10(10,2))