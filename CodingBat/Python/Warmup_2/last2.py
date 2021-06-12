# **********************************************************************************
#   Title: Warmup-2 > last2
#   URL: https://codingbat.com/prob/p145834
#   Date: 12/06/2021
#   Description: 
#     - Given a string, return the count of the number of times that 
#       a substring length 2 appears in the string and also as the 
#       last 2 chars of the string, so "hixxxhi" yields 1 
#       (we won't count the end substring).
#
#       last2('hixxhi') → 1
#       last2('xaxxaxaxx') → 1
#       last2('axxxaaxx') → 2
#************************************************************************************

def last2(str):
    last_two = str[-2:]
    count = 0

    # If you need to traverse a string one step at a time
    # This can be useful, but not ideal O(N) linear time
    for i in range(len(str)-2):
        sub_string = str[i:i+2]
        if sub_string == last_two:
            count += 1

    return count


print(last2('axxxaaxx'))