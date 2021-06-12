# **********************************************************************************
#   Title: List-1 > same_first_last
#   URL: https://codingbat.com/prob/p179078
#   Date: 12/06/2021
#   Description: 
#     - Given an array of ints, return True if the array is length 1 
#       or more, and the first element and the last element are equal.
#************************************************************************************

def same_first_last(nums):
    return nums[:1] == nums[-1:] if len(nums) > 0 else False
  
print(same_first_last([1,2,3,1]))