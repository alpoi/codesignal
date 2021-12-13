# Find the leftmost digit that occurs in a given string.

def solution(inputString):
    for char in inputString:
        if char.isdigit():
            return char

# passed all tests