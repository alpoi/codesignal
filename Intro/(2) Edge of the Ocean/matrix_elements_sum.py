# After becoming famous, the CodeBots decided to move into a new building 
# together. Each of the rooms has a different cost, and some of them are free, 
# but there's a rumour that all the free rooms are haunted! Since the CodeBots 
# are quite superstitious, they refuse to stay in any of the free rooms, or any 
# of the rooms below any of the free rooms.

# Given matrix, a rectangular matrix of integers, where each value represents 
# the cost of the room, your task is to return the total sum of all rooms that 
# are suitable for the CodeBots (ie: add up all the values that don't appear 
# below a 0).

def solution(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0 and i != (len(matrix) - 1):
                matrix[i+1][j] = 0
    return sum([sum(row) for row in matrix])

# passed all tests