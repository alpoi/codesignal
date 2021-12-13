# Ticket numbers usually consist of an even number of digits. A ticket number 
# is considered lucky if the sum of the first half of the digits is equal to 
# the sum of the second half.

# Given a ticket number n, determine if it's lucky or not.

def solution(n):
    
    x = len(str(n))
    h1 = sum([int(char) for char in str(n)[:int(x/2)]])
    h2 = sum([int(char) for char in str(n)[int(x/2):]])
    
    return h1 == h2

# passed all tests