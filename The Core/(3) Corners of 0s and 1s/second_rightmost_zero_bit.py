# Implement the missing code, denoted by ellipses. 
# You may not modify the pre-existing code.
# Presented with the integer n, find the 0-based position of the second 
# rightmost zero bit in its binary representation (it is guaranteed that 
# such a bit exists), counting from right to left.

# Return the value of 2 ** position_of_the_found_bit

def solution(n):
    return 2 ** (bin(n)[::-1].find('0', bin(n)[::-1].find('0') + 1))             # str.find('subs', str.find('subs') + 1) will find the 2nd occurrence

# passed all tests