# Given array of integers, find the maximal possible sum of some of its k 
# consecutive elements.

def solution(x, k):
    return max( [ sum(x[i:i+k] ) for i in range( len(x) - k + 1 )] )

# passed 19/20 tests
# exceeded 4 second execution time limit for final test