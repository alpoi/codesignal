# Given a rectangular matrix of characters, add a border of asterisks(*) to it.
# Example:
#
#  picture = ["abc",
#             "ded"]
#             
#  solution(picture) = ["*****",
#                       "*abc*",
#                       "*ded*",
#                       "*****"]

def solution(picture):
    with_border = [ '*' * (len(picture[0]) + 2) ]
    for elem in picture:
        with_border.append( '*' + elem + '*' )
    with_border.append( '*' * (len(picture[0]) + 2) )
    return with_border

# passed all tests