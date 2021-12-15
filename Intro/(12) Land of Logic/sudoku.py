# Sudoku is a number-placement puzzle. The objective is to fill a 9 × 9 grid 
# with digits so that each column, each row, and each of the nine 3 × 3 
# sub-grids that compose the grid contains all of the digits from 1 to 9.
# 
# This algorithm should check if the given grid of numbers represents a 
# correct solution to Sudoku.

def solution(grid):

    for row in grid:
        for num in range(9):
            if row.count(num + 1) != 1:
                print(f'problem in row {row}')
                return False

    cols = [[row[i] for row in grid] for i in range(9)]
    
    for col in cols:
        for num in range(9):
            if col.count(num + 1) != 1:
                print(f'problem in col {col}')
                return False
    
    blocks = [[] for i in range(9)]
    blocks[0] = [grid[i][j] for i in range(3) for j in range(3)]
    blocks[1] = [grid[i + 3][j] for i in range(3) for j in range(3)]
    blocks[2] = [grid[i + 6][j] for i in range(3) for j in range(3)]
    blocks[3] = [grid[i][j + 3] for i in range(3) for j in range(3)]
    blocks[4] = [grid[i + 3][j + 3] for i in range(3) for j in range(3)]
    blocks[5] = [grid[i + 6][j + 3] for i in range(3) for j in range(3)]
    blocks[6] = [grid[i][j + 6] for i in range(3) for j in range(3)]
    blocks[7] = [grid[i + 3][j + 6] for i in range(3) for j in range(3)]
    blocks[8] = [grid[i + 6][j + 6] for i in range(3) for j in range(3)]

    for block in blocks:
        for num in range(9):
            if block.count(num + 1) != 1:
                print(f'problem in block {block}')
                return False

    return True

# passed all tests