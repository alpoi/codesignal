# Given an array of strings, return another array containing all of its 
# longest strings.

def solution(inputArray):
    return [elem for elem in inputArray if len(elem) == max([len(st) for st in inputArray])]

# passed all tests