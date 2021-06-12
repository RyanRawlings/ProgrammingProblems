# **********************************************************************************
#   Title: String-1 > first_half
#   URL: https://codingbat.com/prob/p107010
#   Date: 12/06/2021
#   Description: 
#     - Given a string of even length, return the first half. So the string 
#       "WooHoo" yields "Woo".
#     - No solution provide on website
#************************************************************************************

def first_half(str):
    return str[:int(len(str)/2)]

print(first_half('WooHoo'))