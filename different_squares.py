# Given a rectangular matrix containing only digits, calculate the number of 
# different 2 × 2 squares in it.
#
# matrix = [ [00, 01, ..., 0n], 
#            [10, 11, ..., 1n],
#            [ .,  ., ..., . ],
#            [m0, m1, ..., mn] ]

def solution(matrix):
    squares = []
    for i in range(len(matrix) - 1):
        for j in range(len(matrix[0]) - 1):
            sq = [ [matrix[i][j], matrix[i][j+1]],
                   [matrix[i+1][j], matrix[i+1][j+1]] ]
            if sq not in squares:
                squares.append(sq)
    return len(squares)

# passed all tests