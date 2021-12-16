# Implement the missing code, denoted by ellipses. 
# You may not modify the pre-existing code.
# You're given an arbitrary 32-bit integer n. Take its binary representation, 
# split bits into it in pairs (bit number 0 and 1, bit number 2 and 3, etc.) 
# and swap bits in each pair. Then return the result as a decimal number.

def solution(n):
    return int(''.join([f'{n:032b}'[i:i+2][::-1] for i in range(0, 32, 2)]), 2)

# passed all tests