# Given array of integers, remove each kth element from it.

def solution(inputArray, k):
    for i in range(k - 1, len(inputArray), k):
        inputArray[i] = "x"
    return [elem for elem in inputArray if elem != "x"]

# passed all tests