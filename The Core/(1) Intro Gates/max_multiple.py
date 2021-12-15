# Given a divisor and a bound, find the largest integer N such that:
# - N is divisible by divisor.
# - N is less than or equal to bound.
# - N is greater than 0.
# It is guaranteed that such a number exists.

def solution(divisor, bound):
    for N in range(bound, 0, -1):
        if N % divisor == 0:
            return N

# passed all tests