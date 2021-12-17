# Given an integer n, find the minimal k such that
# - k = m! (where m! = 1 * 2 * ... * m) for some integer m;
# - k >= n.
# In other words, find the smallest factorial which is not less than n.

def solution(n):
    i, k = 1, 1
    while k < n:
        i += 1
        k *= i
    return k

# passed all tests