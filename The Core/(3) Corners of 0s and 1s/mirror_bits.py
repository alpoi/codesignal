# Reverse the order of the bits in a given integer.

def solution(a):
    return int(f'{a:b}'[::-1], 2)

# passed all tests