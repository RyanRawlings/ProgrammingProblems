# **********************************************************************************
#   Title: Warmup-2 > string_match
#   URL: https://codingbat.com/prob/p182414
#   Date: 12/06/2021
#   Description: 
#     - Given 2 strings, a and b, return the number of the positions 
#       where they contain the same length 2 substring. So "xxcaazz" 
#       and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings 
#       appear in the same place in both strings.
#************************************************************************************

# Python dictionary to hold key value pairs
def string_match(a, b):
    substring_count = 0
    smallest_length = 0

    a_sub_str_index_set = {}
    b_sub_str_index_set = {}

    if len(a) > len(b):
        smallest_length = len(b)
    else:
        smallest_length = len(a)

    for index in range(smallest_length):
        a_substring = a[index:index+2]
        b_substring = b[index:index+2]
        
        a_sub_str_index_set[index] = a_substring
        b_sub_str_index_set[index] = b_substring

        if a_sub_str_index_set[index] == b_sub_str_index_set[index] and len(a_sub_str_index_set[index]) == 2 and len(b_sub_str_index_set[index]) == 2:
            substring_count += 1

    return substring_count

print(string_match('aabbccdd', 'abbbxxd'))