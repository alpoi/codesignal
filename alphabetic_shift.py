# Given a string, your task is to replace each of its characters 
# by the next one in the English alphabet; i.e. replace a with b, 
# replace b with c, etc (z would be replaced by a).

def solution(inputString):
    sol = ''
    for char in inputString:
        if char == 'z':
            sol += 'a' 
        else:
            sol += chr(ord(char) + 1)
    return sol

# caesar cipher
# passed all tests