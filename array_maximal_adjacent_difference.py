# Given an array of integers, find the maximal absolute difference between any two of its adjacent elements.

def solution(inputArray):
    return max([abs(inputArray[i] - inputArray[i + 1]) for i in range(len(inputArray) - 1)])

# passed all tests