# Given a string, return its encoding defined as follows:
#
# - First, the string is divided into the least possible number of disjoint 
#   substrings consisting of identical characters
#   - for example, "aabbbc" is divided into ["aa", "bbb", "c"]
# - Next, each substring with length greater than one is replaced with a 
#   concatenation of its length and the repeating character
#   - for example, substring "bbb" is replaced by "3b"
# - Finally, all the new strings are concatenated together in the same order and 
#   a new string is returned.

def solution(s):
    subs = []
    previous = ''
    for char in s:
        if char == previous:
            subs[-1] += char
        else:
            subs.append(char)
        previous = char
    
    for i in range(len(subs)):
        if len(subs[i]) > 1:
            subs[i] = str(len(subs[i])) + subs[i][0]

    return ''.join(subs)

# passed all tests