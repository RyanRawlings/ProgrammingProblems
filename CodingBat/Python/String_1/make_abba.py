# **********************************************************************************
#   Title: String-1 > make_abba
#   URL: https://codingbat.com/prob/p182144
#   Date: 12/06/2021
#   Description: 
#     - Given two strings, a and b, return the result of putting them 
#       together in the order abba, e.g. "Hi" and "Bye" returns "HiByeByeHi".
#************************************************************************************

# This won't through error for NoneType concatatenation
def make_abba(a,b):
    return '{first}{second}{third}{fourth}'.format(first=a,second=b,third=b,fourth=a)

# Test Case
print(make_abba('Hi','Ryan'))