# Given some integer, find the maximal number you can obtain by deleting 
# exactly one digit of the given number.

def solution(n):
    n = str(n)
    nums = [ n[:i] + n[i+1:] for i in range(len(n)) ]
    return max([int(x) for x in nums])

# passed all tests