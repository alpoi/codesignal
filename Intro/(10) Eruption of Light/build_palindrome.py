# Given a string, find the shortest possible string which can be achieved by 
# adding characters to the end of initial string to make it a palindrome.

def solution(st):
    for i in range(len(st)):
        if st[i:] == st[i:][::-1]:
            return st + st[:i][::-1]

# passed all tests