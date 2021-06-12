# **********************************************************************************
#   Title: List-1 > common_end
#   URL: https://codingbat.com/prob/p147755
#   Date: 12/06/2021
#   Description: 
#     - Given 2 arrays of ints, a and b, return True if they have the 
#       same first element or they have the same last element. Both 
#       arrays will be length 1 or more.
#************************************************************************************

def common_end(a, b):
  return a[-1:] == b[-1:] or a[:1] == b[:1]

print(common_end([1,2,3], [1,3]))