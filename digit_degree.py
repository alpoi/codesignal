# Let's define digit degree of some positive integer as the number of times we 
# need to replace this number with the sum of its digits until we get to a one 
# digit number. Given an integer, find its digit degree.

def solution(n):
    degree = 0
    while n >= 10:
        n = sum( list( map(int, list(str(n))) ) )
        degree += 1
    return degree

# passed all tests