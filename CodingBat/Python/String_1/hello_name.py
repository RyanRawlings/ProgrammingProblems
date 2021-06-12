# **********************************************************************************
#   Title: String-1 > hello_name
#   URL: https://codingbat.com/prob/p115413
#   Date: 12/06/2021
#   Description: 
#     - Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".
#************************************************************************************

# This won't through error for NoneType concatatenation
def hello_name(name):
    return 'Hello {name}!'.format(name=name)

print(hello_name('Ryan'))