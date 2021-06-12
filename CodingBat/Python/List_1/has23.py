# **********************************************************************************
#   Title: List-1 > has23
#   URL: https://codingbat.com/prob/p177892
#   Date: 12/06/2021
#   Description: 
#     - Given an int array length 2, return True if it contains a 2 or a 3.
#************************************************************************************

def has23(nums):
    return 2 in nums or 3 in nums

print(has23([2,4,5]))