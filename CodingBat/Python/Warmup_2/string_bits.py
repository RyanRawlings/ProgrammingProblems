# **********************************************************************************
#   Title: Warmup-2 > string_bits
#   URL: https://codingbat.com/prob/p113152
#   Date: 12/06/2021
#   Description: 
#     - Given a string, return a new string made of every other char 
#       starting with the first, so "Hello" yields "Hlo".
#************************************************************************************

def string_bits(str):
    return_string = ''

    for index in range(0,len(str),1):
        if index % 2 == 0:
            return_string += str[index]

    return return_string

# Test Cases
# print(string_bits('Heeololeo'))
# print(string_bits('Hi'))