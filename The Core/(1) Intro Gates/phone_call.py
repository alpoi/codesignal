# Some phone usage rate may be described as follows:
# - first minute of a call costs min1 cents,
# - each minute from the 2nd up to 10th (inclusive) costs min2_10 cents
# - each minute after 10th costs min11 cents.
# You have s cents on your account before the call. What is the duration of the 
# longest call (in minutes rounded down to the nearest integer) you can have?

def solution(min1, min2_10, min11, s):
    def cost(min):
        if min == 0:
            return min1
        if 0 < min < 10:
            return min2_10
        if min >= 10:
            return min11
    
    total, min = 0, 0
    
    while total <= s:
        total += cost(min) 
        min += 1
        
    return min - 1
        
# passed all tests