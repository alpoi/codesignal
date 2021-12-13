# Given two strings, find the number of common characters between them.

def solution(s1, s2):
    shared = set(s1).intersection(set(s2))
    return sum([min(s1.count(char), s2.count(char)) for char in shared])

# passed all tests