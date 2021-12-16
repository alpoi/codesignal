# Implement the missing code, denoted by ellipses. 
# You may not modify the pre-existing code.

# You're given two integers, n and m. Find position of the rightmost pair of 
# equal bits in their binary representations (it is guaranteed that such a 
# pair exists), counting from right to left.

# Return the value of 2 ** position_of_the_found_pair (0-based).

def solution(n, m):
    return (~(n ^ m)) & -(~(n ^ m))                                              
    
# after brushing up on bitwise operators, found that
# x & -x returns the lowest bit
# and ~(x ^ y) returns 1 if the bit in x equals the bit in y, 0 otherwise

# passed all tests