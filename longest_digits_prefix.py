# Given a string, output its longest prefix which contains only digits.

def solution(inputString):
    prefix = ''
    for char in inputString:
        if char.isdigit():
            prefix += char
        else:
            return prefix
    return prefix # if all the characters are digits

# passed all tests