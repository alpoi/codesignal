# You are given an array of integers. On each move you are allowed to 
# increase exactly one of its element by one. Find the minimal number 
# of moves required to obtain a strictly increasing sequence from the 
# input.

def solution(inputArray):
    count = 0
    for i in range(len(inputArray) - 1):
        if inputArray[i + 1] <= inputArray[i]:
            diff = (inputArray[i] - inputArray[i + 1])
            count += diff + 1
            inputArray[i + 1] += diff + 1
    
    return count

# passed all tests
        


