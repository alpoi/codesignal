# You are given two numbers a and b where 0 ≤ a ≤ b. Imagine you construct an 
# array of all the integers from a to b inclusive. You need to count the number 
# of 1s in the binary representations of all the numbers in the array.

def solution(a, b):
    nums = [f'{x:b}' for x in range(a, b + 1)]
    return sum([bits.count('1') for bits in nums])

# passed all tests