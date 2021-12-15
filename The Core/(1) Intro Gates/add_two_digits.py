# You are given a two-digit integer n. Return the sum of its digits.

def solution(n):
    return sum([int(char) for char in str(n)])

# passed all tests