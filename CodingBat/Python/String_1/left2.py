# **********************************************************************************
#   Title: String-1 > left2
#   URL: https://codingbat.com/prob/p160545
#   Date: 12/06/2021
#   Description: 
#     - Given a string, return a "rotated left 2" version where the first 2 
#       chars are moved to the end. The string length will be at least 2.
#************************************************************************************

def left2(str):
    return str[2:] + str[:2]

print(left2('Test'))