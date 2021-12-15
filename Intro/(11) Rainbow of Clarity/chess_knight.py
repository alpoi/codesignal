# Given a position of a knight on the standard chessboard, find the number of 
# different moves the knight can perform.

# The knight can move to a square that is two squares horizontally and one 
# square vertically, or two squares vertically and one square horizontally away 
# from it. The complete move therefore looks like the letter L. Check out the 
# image below to see all valid moves for a knight piece that is placed on one 
# of the central squares.

def solution(cell):
    files = { "a" : 1, "b" : 2, "c" : 3, "d" : 4, 
              "e" : 5, "f" : 6, "g" : 7, "h" : 8 }
              
    cell = (files[cell[0]], int(cell[1]))

    count = 0

    if 0 < cell[0] + 2 <= 8 and 0 < cell[1] + 1 <= 8:
        count += 1
    if 0 < cell[0] - 2 <= 8 and 0 < cell[1] + 1 <= 8:
        count += 1
    if 0 < cell[0] + 2 <= 8 and 0 < cell[1] - 1 <= 8:
        count += 1
    if 0 < cell[0] - 2 <= 8 and 0 < cell[1] - 1 <= 8:
        count += 1
    if 0 < cell[0] + 1 <= 8 and 0 < cell[1] + 2 <= 8:
        count += 1
    if 0 < cell[0] - 1 <= 8 and 0 < cell[1] + 2 <= 8:
        count += 1
    if 0 < cell[0] + 1 <= 8 and 0 < cell[1] - 2 <= 8:
        count += 1
    if 0 < cell[0] - 1 <= 8 and 0 < cell[1] - 2 <= 8:
        count += 1
    
    return count

# passed all tests