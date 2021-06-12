# **********************************************************************************
#   Title: List-1 > make_ends
#   URL: https://codingbat.com/prob/p124806
#   Date: 12/06/2021
#   Description: 
#     - Given an array of ints, return a new array length 2 containing 
#       the first and last elements from the original array. The original 
#       array will be length 1 or more.
#************************************************************************************

def make_ends(nums):
    return [nums[0], nums[len(nums)-1]]

print(make_ends([1,2,3]))