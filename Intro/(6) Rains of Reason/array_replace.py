# Given an array of integers, replace all the occurrences of elemToReplace with substitutionElem.

def solution(inputArray, elemToReplace, substitutionElem):
    return list(map(lambda x: substitutionElem if x == elemToReplace else x, inputArray))

# passed all tests
# could have just used list comprehension...