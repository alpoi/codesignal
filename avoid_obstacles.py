# You are given an array of integers representing coordinates of obstacles
# situated on a straight line. Assume that you are jumping from the point
# with coordinate 0 to the right. You are allowed only to make jumps of the 
# same length represented by some integer. Find the minimal length of the 
# jump enough to avoid all the obstacles.

# smallest integer that is not a factor of any element in the list

def solution(inputArray):

    for i in range(1, max(inputArray)):
        if all(elem % i != 0 for elem in inputArray):
            return i
                
    return max(inputArray) + 1

# passed all tests