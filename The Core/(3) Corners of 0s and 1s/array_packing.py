# You are given an array of up to four non-negative integers, each less 
# than 256.

# Your task is to pack these integers into one number M in the following way:

# The first element of the array occupies the first 8 bits of M;
# The second element occupies next 8 bits, and so on.
# Return the obtained integer M.

def solution(a):
    packed = ''.join(['{0:08b}'.format(i) for i in a][::-1])                     # 08b converts to 8 bit binary, padded with zeros
    return int(packed, 2)

# passed all tests