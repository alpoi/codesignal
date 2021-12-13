# A string is said to be beautiful if each letter in the string appears at most 
# as many times as the previous letter in the alphabet within the string; ie: b 
# occurs no more times than a; c occurs no more times than b; etc. Note that 
# letter a has no previous letter. Given a string, check whether it is 
# beautiful.

def solution(inputString):
    letters = sorted(set(inputString))
    diff = abs(ord(letters[0]) - ord(letters[-1])) + 1
    if diff != len(letters) or letters[0] != 'a':
        return False # letter missing
    for i in range(len(letters) - 1):
        if inputString.count(letters[i]) < inputString.count(letters[i + 1]):
            return False
    return True

# passed all tests