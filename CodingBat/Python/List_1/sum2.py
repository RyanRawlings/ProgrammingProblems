# **********************************************************************************
#   Title: List-1 > sum2
#   URL: https://codingbat.com/prob/p192589
#   Date: 12/06/2021
#   Description: 
#     - Given an array of ints, return the sum of the first 2 elements in 
#       the array. If the array length is less than 2, just sum up the 
#       elements that exist, returning 0 if the array is length 0.
#************************************************************************************

def sum2(nums):
    if len(nums) >= 2:
        return sum(nums[:2])
    elif len(nums) < 2 and len(nums) != 0: 
        return sum(nums)
    else:
        return 0
    
print(sum2([1,2]))