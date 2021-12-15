# Two arrays are called similar if one can be obtained from another by swapping 
# at most one pair of elements in one of the arrays. Given two arrays a and b, 
# check whether they are similar.

def solution(a, b):

    # only possible if there are exactly 2 differences

    if len(a) != len(b):
        return False

    diff = []
    while len(diff) <= 2:
        for i in range(len(a)):
            if a[i] != b[i]:
                diff.append((a[i], b[i]))

        if len(diff) == 0:
            return True

        if len(diff) != 2:
            return False
   
        if diff[0][0] == diff[1][1] and diff[1][0] == diff[0][1]: # checks if the lists are the same after swapping the differences
            return True
    
    return False

# passed all tests