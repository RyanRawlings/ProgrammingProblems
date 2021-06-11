# **********************************************************************************
#   Title: Warmup-1 > pos_neg
#   URL: https://codingbat.com/prob/p162058
#   Date: 11/06/2021
#   Description: 
#     - Given 2 int values, return True if one is negative and one is positive. 
#       Except if the parameter "negative" is True, then return True only if both are negative.
#************************************************************************************

# Single line solution - might be more beneficial as a conditional
def pos_neg(a,b,negative):
    return (negative == True and a < 0 and b < 0) or (negative == False and a < 0 and b > 0) or ( negative == False and a > 0 and b < 0)

# Test Case
print(pos_neg(10,-10,True))