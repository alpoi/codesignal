# Given an array of equal-length strings, you'd like to know if it's possible 
# to rearrange the order of the elements in such a way that each consecutive 
# pair of strings differ by exactly one character. Return true if it's possible, 
# and false if not. Note: You're only rearranging the order of the strings, 
# not the order of the letters within the strings!

from itertools import permutations

def solution(inputArray):
    perms = list(permutations(inputArray))
    for perm in perms:
        # print(" permutation", perm)
        comparisons = 0
        for i in range(len(perm) - 1):
            # print(f" comparing {perm[i]} with {perm[i + 1]}")
            comparisons += 1
            diff = 0
            for j in range(len(perm[0])):
                if perm[i][j] != perm[i + 1][j]:
                    # print(f" difference: {perm[i][j]} != {perm[i + 1][j]}")
                    diff += 1
                # print(f" diff = {diff}")
                if diff > 1:
                    # print(f" diff > 1, breaking")
                    break
            if diff == 1:
                # print(f" diff == 1 throughout, checking next pair")
                continue 
            else:
                # print(f" finished pair with diff = {diff}, breaking")
                break
        if diff == 1 and comparisons == len(perm) - 1:
            # print(f" made it through every comparison with diff = 1, success!")
            return True
    return False

# passed all tests