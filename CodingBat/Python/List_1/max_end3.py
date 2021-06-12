# **********************************************************************************
#   Title: List-1 > max_end3
#   URL: https://codingbat.com/prob/p135290
#   Date: 12/06/2021
#   Description: 
#     - Given an array of ints length 3, figure out which is larger, 
#       the first or last element in the array, and set all the other 
#       elements to be that value. Return the changed array.
#************************************************************************************

def max_end3(nums):
    return [nums[0], nums[0], nums[0]] if nums[0] > nums[len(nums)-1] else [nums[len(nums)-1],nums[len(nums)-1],nums[len(nums)-1]]

print(max_end3([11,2,8]))