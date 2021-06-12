# **********************************************************************************
#   Title: List-1 > reverse3
#   URL: https://codingbat.com/prob/p192962
#   Date: 12/06/2021
#   Description: 
#     - Given an array of ints length 3, return a new array with the 
#       elements in reverse order, so {1, 2, 3} becomes {3, 2, 1}.
#************************************************************************************

def reverse3(nums):
    return nums[::-1]
    
print(reverse3([1,2,3]))