# **********************************************************************************
#   Title: Warmup-2 > string_times
#   URL: https://codingbat.com/prob/p193507
#   Date: 12/06/2021
#   Description: 
#     - Given a string and a non-negative int n, return a larger string 
#       that is n copies of the original string.
#************************************************************************************

def string_times(str, n):
    return_string = ''

    if n > 0:
        for _ in range(1, n + 1, 1):
            return_string += str

    return return_string

# Test Case
print(string_times('Hi', 2))