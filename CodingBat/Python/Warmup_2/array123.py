# **********************************************************************************
#   Title: Warmup-2 > array_123
#   URL: https://codingbat.com/prob/p193604
#   Date: 12/06/2021
#   Description: 
#     - Given an array of ints, return True if the sequence of 
#       numbers 1, 2, 3 appears in the array somewhere.
#************************************************************************************

def array123(nums):
    sequence_count = 0

    for index in range(len(nums)-2):
        sequence = [nums[index], nums[index+1],nums[index+2]]
        if sequence == [1,2,3]:
            sequence_count += 1
    
    return sequence_count >= 1

# Test Case
# print(array123([1, 1, 2, 1, 2, 3]))