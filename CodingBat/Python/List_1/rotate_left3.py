# **********************************************************************************
#   Title: List-1 > rotate_left3
#   URL: https://codingbat.com/prob/p148661
#   Date: 12/06/2021
#   Description: 
#     - Given an array of ints length 3, return an array with the elements 
#       "rotated left" so {1, 2, 3} yields {2, 3, 1}.
#************************************************************************************

# Can join two lists using concatentation
def rotate_left3(nums):
    return nums[1:] + nums[:1]

print(rotate_left3([1,2,3]))