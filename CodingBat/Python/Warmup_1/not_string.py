# **********************************************************************************
#   Title: Warmup-1 > not_string
#   URL: https://codingbat.com/prob/p189441
#   Date: 11/06/2021
#   Description: 
#     - Given a string, return a new string where "not " has been added to 
#       the front. However, if the string already begins with "not", return 
#       the string unchanged.
#************************************************************************************

def not_string(str):
    # Check if not appears in string at all
    if 'not' in str:
        # Then check if not is at start of string
        if str.index('not') == 0:
            return str
        else:
            return 'not ' + str
    else:
        return 'not ' + str

print(not_string('not'))