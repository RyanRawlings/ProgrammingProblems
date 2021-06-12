# **********************************************************************************
#   Title: String-1 > make_tags
#   URL: https://codingbat.com/prob/p132290
#   Date: 12/06/2021
#   Description: 
#     - The web is built with HTML strings like "<i>Yay</i>" which draws Yay 
#       as italic text. In this example, the "i" tag makes <i> and </i> which 
#       surround the word "Yay". Given tag and word strings, create the HTML 
#       string with tags around the word, e.g. "<i>Yay</i>".
#************************************************************************************

# This won't through error for NoneType concatatenation
def make_tags(tag,word):
    return '<{tag}>{word}</{tag}>'.format(tag=tag,word=word)

# Test Case
print(make_tags('h1','Ryan'))