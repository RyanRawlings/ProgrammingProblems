# **********************************************************************************
#   Title: Warmup-1 > missing_char
#   URL: https://codingbat.com/prob/p149524
#   Date: 12/06/2021
#   Description: 
#     - Given a non-empty string and an int n, return a new string where 
#       the char at index n has been removed. The value of n will be a 
#       valid index of a char in the original string (i.e. n will be in 
#       the range 0..len(str)-1 inclusive).
#************************************************************************************

def missing_char(str,n):
    word = ''

    for index, letter in enumerate(str):
        if index != n:
            word += letter
    
    return word
    

print(missing_char('min', 1))