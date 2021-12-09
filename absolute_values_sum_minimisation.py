# Given a sorted array of integers a, your task is to determine which element 
# of a is closest to all other values of a. In other words, find the element 
# x in a, which minimizes the following sum:
#
# abs(a[0] - x) + abs(a[1] - x) + ... + abs(a[a.length - 1] - x)
#
# If there are several possible answers, output the smallest one.

def solution(a):
    
    def total(x):
        return sum([abs(a[i] - x) for i in range(len(a))])
    
    sums = [(x, total(x)) for x in a]
    mini = []
    for elem in sums:
        if elem[1] == min([elem[1] for elem in sums]):
            mini.append(elem[0])
    
    return min(mini)

# passed all tests