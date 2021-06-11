# **********************************************************************************
#   Title: Warmup-1 > front_back
#   URL: https://codingbat.com/prob/p153599
#   Date: 12/06/2021
#   Description: 
#     - Given a string, return a new string where the first and last chars 
#       have been exchanged.
#************************************************************************************

# Single line ternary and string slice solution
def front_back(str):
  return str[len(str) - 1:] + str[1:-1] + str[:1] if len(str) > 1 else str

print(front_back('a'))