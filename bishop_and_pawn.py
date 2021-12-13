# Given the positions of a white bishop and a black pawn on the standard chess 
# board, determine whether the bishop can capture the pawn in one move.

def solution(bishop, pawn):
    diff = abs(ord(bishop[0]) - ord(pawn[0]))
    return abs(int(bishop[1]) - int(pawn[1])) == diff

    # rationale: pawn diagonal to bishop iff file diff == rank diff

# passed all tests