# Define an integer's roundness as the number of trailing zeroes in it.

# Given an integer n, check if it's possible to increase n's roundness by 
# swapping some pair of its digits.

def solution(n):
    n = str(n)[::-1]
    i = 0
    while n[i] == '0':
        i += 1
    return '0' in n[i + 1:]

# passed all tests