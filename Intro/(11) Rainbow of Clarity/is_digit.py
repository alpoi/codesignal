# Determine if the given character is a digit or not.

def solution(symbol):
    return symbol.isdigit()

# if isdigit() wasn't a built-in string method:
# import re
#
# def solution(symbol):
#     return bool(re.match("^[0-9]$", symbol))

# passed all tests