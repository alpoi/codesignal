# Given two cells on the standard chess board, determine
# whether they have the same colour or not

def solution(cell1, cell2): # colour depends on parity
    return (ord(cell1[0]) + int(cell1[1])) % 2 == (ord(cell2[0]) + int(cell2[1])) % 2

# rationale: colour depends on parity, since it always takes
# two (taxicab) moves to reach another square of the same colour

# passed all tests