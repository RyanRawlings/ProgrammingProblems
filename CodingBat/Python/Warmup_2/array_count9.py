# **********************************************************************************
#   Title: Warmup-2 > array_count9
#   URL: https://codingbat.com/prob/p166170
#   Date: 12/06/2021
#   Description: 
#     - Given an array of ints, return the number of 9's in the array.
#************************************************************************************

def array_count9(nums):
    nine_count = 0
    for number in nums:
        if number == 9:
            nine_count += 1
    
    return nine_count

# Test Case
print(array_count9([1,9,9]))