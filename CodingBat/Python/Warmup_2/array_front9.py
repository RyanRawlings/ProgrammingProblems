# **********************************************************************************
#   Title: Warmup-2 > array_front9
#   URL: https://codingbat.com/prob/p110166
#   Date: 12/06/2021
#   Description: 
#     - Given an array of ints, return True if one of the first 4 elements 
#       in the array is a 9. The array length may be less than 4.
#************************************************************************************

def array_front9(nums):
    nine_count = 0
    for index in range(0, len(nums),1):
        if nums[index] == 9 and index < 4:
            nine_count += 1
    
    return nine_count >= 1

# Test Case
print(array_front9([9, 2, 3]))