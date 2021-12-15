# Given an integer product, find the smallest positive (i.e. greater than 0) 
# integer the product of whose digits is equal to product. If there is no such 
# integer, return -1 instead.

from itertools import permutations

# we require factors to be digits (0-9), and we want as few of them
# as possible (i.e. they should be as large as possible)

def trial(n):
    factors = []
    f = 9                                                                        # start at 9 so we get the larger numbers first

    while n > 9:                                                                 # we want as few digits as possible, so keep n > 9
        if n % f == 0:                                                           # if f is a factor,
            factors.append(f)                                                    # add it to the list,
            n /= f                                                               # and divide it out.
            f = 9                                                                # restart at f == 9
        else:
            f -= 1
            if f == 1:                                                           # n has no more factors less than 10 and greater than 1 (or n == 1)
                if n == 1:                                                       # if n == 1, we reached where we need to be
                    break
                return -1                                                        # otherwise, our task isn't possible and we return -1

    factors.append(int(n))                                                       # since we know n != 1 (we resolved that case on line 22), we append n
    return factors


def solution(n):

    if trial(n) == -1:
        return -1

    if n == 0:                                                                   # special case for zero
        return 10
    if n < 10:                                                                   # special case for n < 10
        return n

    factors = [str(x) for x in trial(n)]

    if len(factors) == 1:                                                        # when n is prime (and larger than 10)
        return -1

    candidates = [int(''.join(perm)) for perm in permutations(factors)]

    return min(candidates)
