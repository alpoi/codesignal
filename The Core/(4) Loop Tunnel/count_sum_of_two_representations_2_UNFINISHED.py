# Given integers n, l and r, find the number of ways to represent n as a sum of 
# two integers A and B such that l ≤ A ≤ B ≤ r.

def solution(n, l, r):
    count = 0
    for i in range(l, r+1):
        for j in range(i, r+1):
            if i + j == n:
                count += 1
    return count

# exceeded time limit on hidden tests

def solution(n, l, r):
    if 2 * r < n or 2 * l > n:
        return 0
    
    A = l
    
    while A + r != n:
        A += 1
        
    count = round((r - A) / 2)
    
    if r + l == n:
        count += 1
        
    return count

# also exceeded time limit on hidden tests