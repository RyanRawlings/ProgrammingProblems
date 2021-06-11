# **********************************************************************************
#   Title: Warmup-1 > sleep_in
#   URL: https://codingbat.com/prob/p173401
#   Date: 11/06/2021
#   Description: 
#     - The parameter weekday is True if it is a weekday, 
#       and the parameter vacation is True if we are on vacation. 
#       We sleep in if it is not a weekday or we're on vacation. 
#       Return True if we sleep in.
#************************************************************************************

def sleep_in(weekday,vacation):
    if weekday == True and vacation == False:
        return False
    else:
        return True

# Can be shortened to 
# return (not weekday or vacation)

# Test Case
print(sleep_in(True, True))