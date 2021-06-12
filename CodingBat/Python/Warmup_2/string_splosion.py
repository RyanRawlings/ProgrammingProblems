# **********************************************************************************
#   Title: Warmup-2 > string_splosion
#   URL: https://codingbat.com/prob/p118366
#   Date: 12/06/2021
#   Description: 
#     - Given a non-empty string like "Code" return a string like "CCoCodCode".
#************************************************************************************

def string_splosion(str):
    return_string = ''
    for index in range(0,len(str)+1,1):
        return_string += str[:index]
    
    return return_string

print(string_splosion('Code'))