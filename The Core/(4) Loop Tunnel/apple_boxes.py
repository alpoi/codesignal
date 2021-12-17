# You have k apple boxes full of apples. Each square box of size m contains 
# m × m apples. You just noticed two interesting properties about the boxes:

# - The smallest box is size 1, the next one is size 2,..., all the way up to 
# size k.
# - Boxes that have an odd size contain only yellow apples. Boxes that have an 
# even size contain only red apples.

# Your task is to calculate the difference between the number of red apples 
# and the number of yellow apples.

def solution(k):
    red = 0
    yellow = 0
    for m in range(k + 1):
        if m % 2 == 1:
            yellow += m ** 2
        else:
            red += m ** 2
    return red - yellow
        
# passed all tests