# **********************************************************************************
#   Title: Warmup-2 > front_times
#   URL: https://codingbat.com/prob/p165097
#   Date: 12/06/2021
#   Description: 
#     - Given a string and a non-negative int n, we'll say that the front of 
#       the string is the first 3 chars, or whatever is there if the string 
#       is less than length 3. Return n copies of the front;
#************************************************************************************

# Single line solution
def front_times(str, n):
    return ''.join(str[:3]*n)

# Test Case
print(front_times('abcd', 2))