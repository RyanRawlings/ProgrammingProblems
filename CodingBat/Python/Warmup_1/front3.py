# **********************************************************************************
#   Title: Warmup-1 > front3
#   URL: https://codingbat.com/prob/p147920
#   Date: 12/06/2021
#   Description: 
#     - Given a string, we'll say that the front is the first 3 chars 
#       of the string. If the string length is less than 3, the front 
#       is whatever is there. Return a new string which is 3 copies 
#       of the front.
#************************************************************************************

# String Slice Indexing
def front3(str):
    return str[:3] + str[:3] + str[:3]

print(front3('CSharpDotNet'))