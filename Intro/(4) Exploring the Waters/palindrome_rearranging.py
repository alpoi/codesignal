# Given a string, find out if its characters can be rearranged to form a palindrome.

def solution(inputString):

# rationale: at most one character can appear an odd number of times

    letters = []
    for char in inputString:
        if char not in letters:
            letters.append(char)

    
    count = [1 if inputString.count(char) % 2 == 1 else 0 for char in letters]

    # sum(count) is the number of characters that appear an odd number of times

    return True if sum(count) <= 1 else False

# passed all tests
