# **********************************************************************************
#   Title: List-1 > first_last6
#   URL: https://codingbat.com/prob/p181624
#   Date: 12/06/2021
#   Description: 
#     - Given an array of ints, return True if 6 appears as either the 
#       first or last element in the array. The array will be length 1 or more.
#************************************************************************************

def first_last6(nums):
  return nums[0] == 6 or nums[len(nums)-1] == 6

print(first_last6([1,2,3,6]))