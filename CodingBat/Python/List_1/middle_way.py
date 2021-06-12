# **********************************************************************************
#   Title: List-1 > middle_way
#   URL: https://codingbat.com/prob/p171011
#   Date: 12/06/2021
#   Description: 
#     - Given 2 int arrays, a and b, each length 3, return a new array 
#       length 2 containing their middle elements.
#************************************************************************************

def middle_way(a, b):
    return [a[int(len(a)/2)], b[int(len(b)/2)]]

print(middle_way([1,2,3],[4,5,6]))