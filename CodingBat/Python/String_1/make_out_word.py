# **********************************************************************************
#   Title: String-1 > make_out_word
#   URL: https://codingbat.com/prob/p129981
#   Date: 12/06/2021
#   Description: 
#     - Given an "out" string length 4, such as "<<>>", and a word, 
#       return a new string where the word is in the middle of the out 
#       string, e.g. "<<word>>".
#************************************************************************************

# This won't through error for NoneType concatatenation
def make_out_word(out,word):
    return '{first_out}{word}{second_out}'.format(first_out=out[:int(len(out)/2)],word=word,second_out=out[-int(len(out)/2):])

# Test Case
print(make_out_word('<<>>','Ryan'))